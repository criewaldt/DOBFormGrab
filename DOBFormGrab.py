#DOBFormGrab
from bs4 import BeautifulSoup
import requests


with open("dobForms.mhtml") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

links = soup.find_all('a')
for l in links:

    g = l.string
    if g is not None:

        if "Form" in g:
            g = g.replace('/', '-')
            r = requests.get("https://www.nyc.gov/{}".format(l['href']), allow_redirects=True)

            with open("Forms/{}.pdf".format(g), 'wb') as pdf:
                pdf.write(r.content)
            
            print('Downloaded: {}'.format(g))