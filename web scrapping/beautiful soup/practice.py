import requests
from bs4 import BeautifulSoup
url="https://codewithharry.com"
r = requests.get(url)
htmlcontent = r.content
soup = BeautifulSoup(htmlcontent, 'html.parser')
# print(soup.prettify)
title=soup.title
print(title)
