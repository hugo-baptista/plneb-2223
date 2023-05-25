import requests, json, re
from bs4 import BeautifulSoup

disease_dic = {}

url = 'https://www.atlasdasaude.pt/doencasAaZ'
html = requests.get(url).text

soup = BeautifulSoup(html, 'html.parser')

diseases = soup.find_all('div', class_='views-row')

for disease in diseases:
    title = disease.find('div', class_='views-field-title').text
    title = re.sub(r"^ +", "", title);
    title = re.sub(r" +$", "", title);
    designation = disease.find('div', class_='views-field-body').text
    designation = re.sub(r"^ +", "", designation);
    designation = re.sub(r" +$", "", designation);
    # print(f'Title: {title}\nDesignation: {designation}\n')
    disease_dic[title] = designation

file = open('./trabalhos_aulas/aula_9/db-diseases-A.json', 'w', encoding='utf-8')
json.dump(disease_dic, file, indent=4, ensure_ascii=False)
file.close()