import requests, json, re
from bs4 import BeautifulSoup

def getDiseasePage(base_url, disease):
    href = disease.find('div', class_='views-field-title').a.get('href')
    html = requests.get(base_url+href).text
    soup = BeautifulSoup(html, 'html.parser')
    page = soup.find('div', class_='field field-name-body field-type-text-with-summary field-label-hidden')
    res = page.div.div
    res.name = "page"
    res.attrs = {}
    return str(res)

def getDisease(disease):
    title = disease.find('div', class_='views-field-title').text
    designation = disease.find('div', class_='views-field-body').text
    return title.strip(), designation.strip()

base_url = 'https://www.atlasdasaude.pt'
page_url = '/doencasAaZ'
main_html = requests.get(base_url+page_url).text
main_soup = BeautifulSoup(main_html, 'html.parser')

disease_dic = {}
divs = main_soup.find_all('div', class_='views-summary views-summary-unformatted')
for div in divs[:1]:
    href = div.a.get('href')
    html = requests.get(base_url+href).text
    soup = BeautifulSoup(html, 'html.parser')

    diseases = soup.find_all('div', class_='views-row')
    for disease in diseases[:1]:
        title, designation = getDisease(disease)
        page = getDiseasePage(base_url, disease)
        disease_dic[title] = {
            'desc': designation,
            'page': page
        }

file = open('./trabalhos_aulas/aula_9/db-complete.json', 'w', encoding='utf-8')
json.dump(disease_dic, file, indent=4, ensure_ascii=False)
file.close()