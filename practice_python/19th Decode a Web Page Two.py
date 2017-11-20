# Using the requests and BeautifulSoup Python libraries, print to the screen the full text of
# the article on this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.
#The article is long, so it is split up between 4 pages. Your task is to print out the text to the screen
# so that you can read the full article without having to click any buttons.

from bs4 import BeautifulSoup
import requests
url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)

#r_html = r.text

soup= BeautifulSoup(r.content, "lxml")

#print(soup.find_all(name="span"))
text=[]
for span in soup.find_all('p'):
    text.append(span.text)
print(len(text))
for i in text:
    print(i)

#print(soup.prettify())

#<span itemprop="name">34 plakanın diğer illerdeki karizması</span>

