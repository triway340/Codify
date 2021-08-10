#Code By Triway

try:
    import base64
    import os
    import platform 
    import time
    from colorama import init, Fore
except ModuleNotFoundError:
    if platform.system() == "Windows":
        print("\nEsta instalacion solo pasa una vez...\n")
        time.sleep(1)
        os.system("python -m pip install colorama")
    else:
        print("\nEsta instalacion solo pasa una vez...\n")
        time.sleep(1)
        os.system("python3 -m pip install colorama")
YELLOW = Fore.YELLOW
RED = Fore.RED
CYAN = Fore.CYAN
BLUE = Fore.BLUE
RESET = Fore.WHITE
GREEN = Fore.GREEN
banner = RED+'''
    ░░░░░░░░░░░║
    ░░▄█▀▄░░░░░║░░░░░░▄▀▄▄
    ░░░░░░▀▄░░░║░░░░▄▀
    ░▄▄▄░░░░█▄▄▄▄▄▄█░░░░▄▄▄
    ▀░░░▀█░█▀░░▐▌░░▀█░█▀░░░▀
    ░░░░░░██░░▀▐▌▀░░██
    ░▄█▀▀▀████████████▀▀▀█
    █░░░░░░██████████░░░░░▀▄
    █▄░░░█▀░░▀▀▀▀▀▀░░▀█░░░▄█
    ░▀█░░░█░░░░░░░░░░█░░░█▀
    
            By: Osay
'''
def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
init(autoreset=False)
def encode():
    while True:
        clear()
        print(banner)
        print(RESET+"")
        try:
            b64text = input("\nIngrese el texto a codificar ---> ")
        except:
            print(GREEN+"\nHa ocurrido un error...")
            print(RED+"\nSaliendo...\n")
            exit()
        if b64text=="":
            print(GREEN+"\nIngrese un texto a codificar.")
            time.sleep(5)
            break
        str64 = b64text.encode("utf-8")
        base64_bytes = base64.b64encode(str64)
        print(f"\n{RED}Su texto codificado es: {CYAN}{base64_bytes}{RESET}")
        extra1 = input("\nPresione enter para continuar...")
        break
def decode():
    while True:
            try:
                clear()
                print(banner)
                print(RESET+"")
                texto = input('\nTexto a descodificar --->  ')
                if texto=="":
                    print(GREEN+"\nIngrese el texto codificado a descodificar.")
                    time.sleep(5)
                    break
                texto_encode = base64.b64decode(texto.encode())
                result=(texto_encode.decode())
                print(f"\n{RED}Su Texto Es : {CYAN}" +result, f"{RESET}")
                extra2 = input("\nPresione enter para continuar... ")
                break
            except:
                print(GREEN+"\nIngrese un texto codificado valido.")
                time.sleep(5)
def home():
    while True:
        clear()
        print(banner)
        print(f"{RESET}[ {BLUE}1 {RESET}] {BLUE}- {CYAN}Codificar ")
        print(f"{RESET}[ {BLUE}2 {RESET}] {BLUE}- {CYAN}Descodificar")
        print(f"{RESET}[ {BLUE}X {RESET}] {BLUE}- {CYAN}Salir{YELLOW}")
        peticion = input(f"\nIngrese una opción ---> ")
        if peticion=="1":
            clear()
            print(RESET+"")
            encode()
        elif peticion=="2":
            clear()
            print(RESET+"")
            decode()
        elif peticion=="x" or peticion=="X":
            print(RED+"\nOkey adios...")
            exit()
        else:
            clear()
            print(GREEN+"\nOpcion incorrecta.")
            time.sleep(2)
            print(RED+"\nVolviendo...")
            time.sleep(2)
home()

#Code By Triway
