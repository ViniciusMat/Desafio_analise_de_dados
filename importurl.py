import requests
import pandas
import json
# def ler_arquivo_json(jason):
with open('municipios.json', encoding='utf-8') as meu_json:
    dados = json.load(meu_json)
    from pandas import json_normalize
    df = json_normalize(dados['data'])
    print(df)


