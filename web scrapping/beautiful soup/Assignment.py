import requests
from bs4 import BeautifulSoup
r = requests.get('https://www.iitk.ac.in/new/iitk-faculty')
soup = BeautifulSoup(r.content, 'html.parser')
s = soup.find_all('div', class_='jwts_content')
content = s.find_all('p')
for info in content:
    print(info.text)





#name
# print(f'Prof. Name:{soup.title.text}')
# info_1=s.find('p', align="left")
# #contacts
# for info in info_1:
#     print(info.text)
# # #info
# info_3=s.find_all('td', colspan='2', valign='top')
# for Department in info_3:
#     print(Department.text)

















#Name of Prof.
#info_1 = s.find_all('h3', class_='head1')
# for name in info_1:
#print(info_1.text)
#  
# info_2 = s.find_next('p', class_='fac-email')
# #for email in info_3:
# print(info_2.text)

# info_3 = s.find_all('p', class_='ri-heading')
# for interest in info_3:
#     print(interest.text)
