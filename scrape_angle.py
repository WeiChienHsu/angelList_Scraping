from bs4 import BeautifulSoup
import requests

source = requests.get('https://angel.co/companies?company_types[]=Incubator').text

soup = BeautifulSoup(source, 'html.parser')

companies = soup.find_all('div', class_ = 'dc59')

print(type(companies))
print(len(companies))