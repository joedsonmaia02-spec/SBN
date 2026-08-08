import json

def import_dicionario():
    with open('dict.json', 'r') as json_dump:
        dicionario = json.load(json_dump)
    return dicionario