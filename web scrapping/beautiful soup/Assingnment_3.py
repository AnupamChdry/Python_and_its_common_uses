import requests
from bs4 import BeautifulSoup
import pandas as pd
r = requests.get('https://www.iitk.ac.in/new/iitk-faculty')
soup = BeautifulSoup(r.content, 'html.parser')
s = soup.find_all('p', align="left")
for info in s:
    #print(info.text)
    df = pd.DataFrame(ans)
    df.to_csv('output.csv')
    df.head



















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
