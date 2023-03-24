from deep_translator import GoogleTranslator
import json

file_dic = open("trabalhos_aulas/aula_5/dicionario.json")
dic = json.load(file_dic)
file_dic.close()

en_file = open("plneb-2223/data/termos_traduzidos.txt")
en_txt = en_file.read().splitlines()
en_file.close()

dic_pt_en = {}
for entry in en_txt:
    lista = entry.split(" @ ")
    dic_pt_en[lista[0]] = en = lista[1]

new_dic = {}
for termo, explicacao in dic.items():
    if termo in dic_pt_en.keys():
        new_dic[termo] = {
            "des": explicacao,
            "en": dic_pt_en[termo]
        }
    else:
        new_dic[termo] = {
            "des": explicacao,
            "en": GoogleTranslator(source='pt', target='en').translate(termo)
        }

new_file_dic = open("trabalhos_aulas/aula_5/dicionario_pt_en_completo.json", "w", encoding="utf-8")
json.dump(new_dic, new_file_dic, ensure_ascii=False, indent=4)
new_file_dic.close()