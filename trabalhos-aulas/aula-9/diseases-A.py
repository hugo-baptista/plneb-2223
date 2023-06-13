import requests, json, re
from bs4 import BeautifulSoup

url = 'https://www.atlasdasaude.pt/doencasAaZ'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

disease_dic = {}
diseases = soup.find_all('div', class_='views-row')
for disease in diseases:
    title = disease.find('div', class_='views-field-title').text
    designation = disease.find('div', class_='views-field-body').text
    # print(f'Title: {title}\nDesignation: {designation}\n')
    disease_dic[title.strip()] = designation.strip()

file = open('./trabalhos-aulas/aula-9/db-A.json', 'w', encoding='utf-8')
json.dump(disease_dic, file, indent=4, ensure_ascii=False)
file.close()