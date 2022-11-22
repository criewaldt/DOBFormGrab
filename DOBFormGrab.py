#DOBFormGrab
from bs4 import BeautifulSoup
import requests

#local html file with links to download
STATIC_FILE = "dobForms.mhtml"

def download_form(name=None, url=None):
    name = name.replace('/', '-')
    r = requests.get("https://www.nyc.gov/{}".format(url), allow_redirects=True)

    with open("Forms/{}.pdf".format(name), 'wb') as pdf:
        pdf.write(r.content)
    
    print('Downloaded: {}'.format(name))

class DOBFormGrab():
    def local(self, f=STATIC_FILE):
        with open(f) as fp:
            soup = BeautifulSoup(fp, 'html.parser')

        links = soup.find_all('a')
        for l in links:

            name = l.string
            url = l['href']

            if name is not None:

                if "Form" in name:
                    download_form(name, url)  
    
    def web(self, url="https://www.nyc.gov/site/buildings/dob/forms.page"):
        r = requests.get(url, allow_redirects=True)
        soup = BeautifulSoup(r.content, 'html.parser')

        links = soup.find_all('a')
        for l in links:

            name = l.string
            url = l['href']

            if name is not None:

                if "Form" in name:
                    download_form(name, url)


if __name__ == "__main__":
    get_forms = DOBFormGrab()
    get_forms.web()