import json
from traceback import print_tb

path = "./config/perfiles.json"

def getPerfilesNombre():
    perfiles = []

    file = open(path, 'r')
    perfilesJson = json.load(file)
    for j in perfilesJson:
        # print(j)
        perfiles.append(j)

    return perfiles

def getComandosPerfil(perfil):
    comandos = []

    file = open(path, 'r')
    perfilesJson = json.load(file)
    comandos = perfilesJson[perfil]

    return comandos

def setComando(perfil, comando, remplazar):

    existe = False
    with open(path, 'r') as file:
        perfiles = json.load(file)

    if perfil in perfiles:
        comandos = getComandosPerfil(perfil)

        for c in comandos:
            if comando['tecla'] == c['tecla']:
                existe = True
                if remplazar:
                    c['comando'] = comando['comando']
                    c['parametro'] = comando['parametro']

        if not existe:
            comandos.append(comando)

        perfiles[perfil] = comandos
        
    else:
        comandos = []
        comandos.append(comando)
        perfiles[perfil] = comandos
        
    
    with open(path, "w") as file:
        json.dump(perfiles, file)

def teclaConComando(perfil, tecla):
    tieneComando = False

    with open(path, 'r') as file:
        perfiles = json.load(file)

    if perfil in perfiles:
        comandos = perfiles[perfil]
        for c in comandos:
            if tecla == c['tecla']:
                tieneComando = True
                exit

    return tieneComando

def getComando(perfil, tecla):
    comando, param = None, None

    with open(path, 'r') as file:
        perfiles = json.load(file)

    if perfil in perfiles:
        comandos = perfiles[perfil]
        for c in comandos:
            if tecla == c['tecla']:
                comando = c['comando']
                param = c['parametro']

    return comando, param

def setPerfil(perfilNombre):
    ok = False
    perfilesExistentes = getPerfilesNombre()

    if not perfilNombre in perfilesExistentes:
        with open(path, 'r') as file:
            perfiles = json.load(file)

        perfiles[perfilNombre] = []

        with open(path, "w") as file:
            json.dump(perfiles, file)

        ok = True

    return ok

def delPerfil(perfilNombre):
    ok = False
    perfilesExistentes = getPerfilesNombre()

    if perfilNombre in perfilesExistentes:
        with open(path, 'r') as file:
            perfiles = json.load(file)

        del perfiles[perfilNombre]

        with open(path, "w") as file:
            json.dump(perfiles, file)

        ok = True

    return ok



# print(getPerfilesNombre())
# print(getComandosPerfil('PERFIL1'))

# accion = {
#     "tecla": None,
#     "comando": None,
#     "parametro": None
# }

# accion["tecla"] = "J"
# accion["comando"] = "test"
# accion["parametro"] = "test01"

# setComando('PERFIL3', accion)

# print(teclaConComando('PERFIL1', 'A'))
# print(teclaConComando('PERFIL1', 'L'))
# print(teclaConComando('PERFIL2', 'F'))
# print(teclaConComando('PERFIL3', 'B'))