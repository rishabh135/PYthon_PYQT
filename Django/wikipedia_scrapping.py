from urllib.request import urlopen
import urllib.request as req
import webbrowser
import urllib3

from bs4 import BeautifulSoup

proxy = req.ProxyHandler({"https://arisahbh:bash@potter@nknproxy.iitk.ac.in:3128"})
auth = req.HTTPBasicAuthHandler()
opener = req.build_opener(proxy, auth, req.HTTPSHandler)
print('enter=next article, y=open artcle, x=exit')
print('-------------------------------------------')
while True:
    content = urlopen('http://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=10&format=xml')
    xml = content.read()
    content.close()
    soup = BeautifulSoup(xml, "html.parser")
    links = soup.findAll('page')
    for l in links:
        choice = input('Would you like to read about ' + l.get('title').encode('ascii', 'ignore') + '?')
        if choice == 'yes':
            webbrowser.open_new_tab('http://en.wikipedia.org/wiki?curid=' + l.get('id'))
        elif choice == 'x':
            exit(0)
