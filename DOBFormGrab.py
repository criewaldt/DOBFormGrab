#DOBFormGrab
from bs4 import BeautifulSoup
import requests
import os


FORMS_URL = "https://www.nyc.gov/site/buildings/dob/forms.page"
OUTPUT_FOLDER = os.path.abspath("Forms")

#create output folder if it doesnt exist
exists = os.path.exists(OUTPUT_FOLDER)
if not exists:
    os.makedirs(OUTPUT_FOLDER)
print("Forms will be downloaded into: {}".format(OUTPUT_FOLDER))

#helper to download form
def download_form(name=None, url=None):
    r = requests.get("https://www.nyc.gov/{}".format(url), allow_redirects=True)
    with open(os.path.join(OUTPUT_FOLDER ,"{}.pdf".format(name)), 'wb') as pdf:
        pdf.write(r.content)
        print('Downloaded: {}'.format(name))

#helper to clean links
def clean_links(links=None):
    clean_links = []
    for l in links:
        name = l.string
        url = l['href']

        if name is not None:
            if "Form" in name:
                #clean name
                name = name.replace('/', '-')
                clean_links.append({'name':name,'url':url})
    return clean_links


class DOBFormGrab():

    def __init__(self):
        r = requests.get(FORMS_URL, allow_redirects=True)
        self.status_code = r.status_code        
        soup = BeautifulSoup(r.content, 'html.parser')
        self.links = soup.find_all('a')
    
    def grab(self):
        links = clean_links(self.links)
        for link in links:
            download_form(link['name'], link['url'])  


if __name__ == "__main__":
    forms = DOBFormGrab()
    forms.grab()