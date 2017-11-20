from bs4 import BeautifulSoup
import requests


url = 'http://www.nytimes.com'
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")

headings = soup.findAll(class_='story-heading')
text=[]

for link in headings:
    if link.a:
        text.append(link.a.text.replace("\n", " ").strip()) #strip() clears whitespaces
    else:
        text.append(link.contents[0].replace("\n", " ").strip())
basliklar=text
print(len(basliklar))
for i in basliklar:
    print(i)




'''url= 'http://nytimes.com'
r=requests.get(url)
soup= BeautifulSoup(r.content, "lxml")

#print(soup.find_all(name="span"))
text=[]
for link in soup.find_all(name="span"):
    if not "↻"  in link:
        text.append(link.text)
basliklar=text
print(len(basliklar))
for i in basliklar:
    print(i)'''
