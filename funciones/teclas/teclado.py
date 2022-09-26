import keyboard

def ejecutarMacro(macro):
    print(macro)
    if macro != '':
        print("se ejecuto la macro ({})".format(macro))
        keyboard.press_and_release(macro)
    else:
        print("no se registro una macro para esta tecla")

def grabarMacro(indexMacro):

    print("Presiona la macro")
    macro = keyboard.read_hotkey()
    # macros[indexMacro] = macro
    print('macro:{}'.format(macro))

    return macro

def escribir(frase):
    print(f'escribiendo... ({frase})')
    keyboard.write(frase)
    print('escrito')