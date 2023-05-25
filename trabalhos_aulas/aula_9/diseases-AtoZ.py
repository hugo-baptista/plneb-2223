import requests, json
from bs4 import BeautifulSoup

disease_dic = {}

base_url = 'https://www.atlasdasaude.pt'
page_url = '/doencasAaZ'
main_html = requests.get(base_url+page_url).text

main_soup = BeautifulSoup(main_html, 'html.parser')

divs = main_soup.find_all('div', class_='views-summary views-summary-unformatted')

for div in divs:
    page_url = div.a.get('href')

    html = requests.get(base_url+page_url).text

    soup = BeautifulSoup(html, 'html.parser')

    diseases = soup.find_all('div', class_='views-row')

    for disease in diseases:
        title = disease.find('div', class_='views-field-title').text
        designation = disease.find('div', class_='views-field-body').text
        # print(f'Title: {title}\nDesignation: {designation}\n')
        disease_dic[title] = designation

file = open('./trabalhos_aulas/aula_9/db-diseases-AtoZ.json', 'w', encoding='utf-8')
json.dump(disease_dic, file, indent=4, ensure_ascii=False)
file.close()