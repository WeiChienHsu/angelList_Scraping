from bs4 import BeautifulSoup
import requests

source = requests.get('https://github.com/WeiChienHsu/Java_Practice').text

soup = BeautifulSoup(source, 'html.parser')

for problem in soup.find_all('td', class_ = 'content'):
    problem_list = problem.get_text()
    print(problem_list)
    print("-----")