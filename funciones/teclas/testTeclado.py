import keyboard

macros = {
    "btn1": "",
    "btn2": ""
}

def ejecutarMacro(macro):
    if macro != '':
        print("se ejecuto la macro ({})".format(macros[macro]))
        keyboard.press_and_release(macro)
    else:
        print("no se registro una macro para esta tecla")

def macro1():
    print("Presiona la macro")
    macro = keyboard.read_hotkey()
    macros["btn1"] = macro
    print('macro:{}'.format(macros["btn1"]))

def macro2():
    print("Presiona la macro")
    macros["btn2"] = keyboard.read_hotkey()
    print('macro:{}'.format(macros["btn2"]))
        






# def macro1():
#     print("Presiona la macro")
#     macro = keyboard.read_hotkey()
#     print('macro:', macro)
#     keyboard.add_hotkey() (macro, on_triggered('macro 1'))

# def macro2():
#     print("Presiona la macro")
#     macro = keyboard.read_hotkey()
#     print('macro:', macro)
#     keyboard.add_hotkey(macro, on_triggered('macro 2'))