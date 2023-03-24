from deep_translator import GoogleTranslator
import json

file_dic = open("trabalhos_aulas/aula_5/dicionario.json")
dic = json.load(file_dic)
file_dic.close()

new_dic = {}
for termo, explicacao in dic.items():
    new_dic[termo] = {
        "des": explicacao,
        "en": GoogleTranslator(source='pt', target='en').translate(termo),
        "de": GoogleTranslator(source='pt', target='de').translate(termo)
    }

new_file_dic = open("trabalhos_aulas/aula_5/dicionario_traduzido.json")
json.dump(new_dic, new_file_dic, ensure_ascii=False, indent=4)
new_file_dic.close()