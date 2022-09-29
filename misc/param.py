import json

path = 'config/parametros.json'

def getCOMParam():
    pCOM = None
    with open(path, 'r') as file:
        parametros = json.load(file)
        pCOM = parametros["puerto"]
    
    return pCOM

def getPerfilPre():
    perfil = None
    with open(path, 'r') as file:
        parametros = json.load(file)
        perfil = parametros["perfil"]
    
    return perfil