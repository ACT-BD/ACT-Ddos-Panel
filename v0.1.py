##############################
# ACTDDoS Made by 5PY_Z0N3   #
##############################

import socket
import os
import requests
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxies.txt').readlines()
bots = len(proxys)

def ascii_vro():
    clear()
    print(f'''
     / **/|        
     | == /        
      |  |         
      |  |         
      |  /         
       |/  







    ''')
    time.sleep(0.6)
    clear()
    print(f'''



     / **/|        
     | == /        
      |  |         
      |  |         
      |  /         
       |/  


    ''')
    time.sleep(0.6)
    clear()
    print(f'''







     / **/|        
     | == /        
      |  |                  

    ''')
    time.sleep(0.6)
    clear()
    print(f"""

     _.-^^---....,,--       
 _--                  --_  
<                        >)
|                         | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____
    """)
    time.sleep(0.8)
    clear()

def si():
    print('         \x1b[38;2;0;255;255m[ \x1b[38;2;233;233;233mACT \x1b[38;2;0;255;255m] | \x1b[38;2;233;233;233mWelcome to ACT-DDoS PANEL \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mOwner: 5PY_Z0N3 \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mUpdate v0.1')
    print("")

def tools():
    clear()
    si()
    print(f'''
                   \x1b[38;2;0;212;14m╔═══════════════╗
                  \x1b[38;2;0;212;14m ║      \x1b[38;2;0;255;255mTools    \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╔═══╩═══════════════╩═══╗
               \x1b[38;2;0;212;14m║         \x1b[38;2;0;255;255mcrash         \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╚═══════════════════════╝
''')

def menu():
    sys.stdout.write(f"         \x1b]2;ACT V0.1 --> Stars: [{bots}] | Online Users: [1]\x07")
    clear()
    print('\x1b[38;2;0;255;255m[ \x1b[38;2;233;233;233mACT \x1b[38;2;0;255;255m] | \x1b[38;2;233;233;233mWelcome to ACT-DDoS PANEL! \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mOwner: 5PY_Z0N3 \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mUpdate v0.1')
    print("")
    print("""
                \x1b[38;2;0;212;14m╔═══════════\x1b[38;2;0;186;45m════════\x1b[38;2;0;150;88m═══════\x1b[38;2;0;113;133m═════\x1b[38;2;0;83;168m═════\x1b[38;2;0;49;147m══════════╗
                \x1b[38;2;0;212;14m║         \x1b[38;2;239;239;239mWelcome to ACT V0.1 DDoS Panel       \x1b[38;2;0;49;147m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;49;147m- - - - - - \x1b[38;2;239;239;239mFree DDoS Panel 2024\x1b[38;2;0;212;14m- - - - - - -\x1b[38;2;0;49;147m║
                \x1b[38;2;0;212;14m╚═══════════\x1b[38;2;0;186;45m════════\x1b[38;2;0;150;88m═══════\x1b[38;2;0;113;133m═════\x1b[38;2;0;83;168m═════\x1b[38;2;0;49;147m══════════╝
                    \x1b[38;2;0;212;14m╔═══════\x1b[38;2;0;186;45m════════\x1b[38;2;0;150;88m═══════\x1b[38;2;0;113;133m═════\x1b[38;2;0;83;168m═════\x1b[38;2;0;49;147m══════╗
                    \x1b[38;2;0;212;14m║ \x1b[38;2;239;239;239mhttps://t.me\AdvancedCyberTech_BD    \x1b[38;2;0;49;147m║
                    \x1b[38;2;0;212;14m╚═══════\x1b[38;2;0;186;45m════════\x1b[38;2;0;150;88m═══════\x1b[38;2;0;113;133m═════\x1b[38;2;0;83;168m═════\x1b[38;2;0;49;147m══════╝
                \x1b[38;2;0;212;14m╔═══════════\x1b[38;2;0;186;45m════════\x1b[38;2;0;150;88m═══════\x1b[38;2;0;113;133m═════\x1b[38;2;0;83;168m═════\x1b[38;2;0;49;147m══════════╗
                \x1b[38;2;0;212;14m║   \x1b[38;2;239;239;239m     crash <url> METHODS<GET/POST>         \x1b[38;2;0;49;147m║
                \x1b[38;2;0;212;14m╚═══════════\x1b[38;2;0;186;45m════════\x1b[38;2;0;150;88m═══════\x1b[38;2;0;113;133m═════\x1b[38;2;0;83;168m═════\x1b[38;2;0;49;147m══════════╝
""")

def main():
    menu()
    while(True):
        cnc = input('''\x1b[38;2;0;212;14m╔══[V0.1\x1b[38;2;0;186;45m@A\x1b[38;2;0;150;88mC\x1b[38;2;0;113;133mT\x1b[38;2;0;49;147m]
\x1b[38;2;0;212;14m╚\x1b[38;2;0;186;45m═\x1b[38;2;0;150;88m═\x1b[38;2;0;113;133m═\x1b[38;2;0;83;168m═\x1b[38;2;0;49;147m➤ \x1b[38;2;239;239;239m''')
        if cnc == "tools" or cnc == "TOOLS":
            tools()

# TOOLS  METHODS
 
        elif "crash" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run ACT.go -site {url} -data {method}')
            except IndexError:
                print('Usage: crash <url> METHODS<GET/POST>')
                print('Example: crash http://example.com GET')

# TOOLS
        elif "act" in cnc:
            print(f'''
TOOLS  ► SHOW TOOLS METHODS
            ''')

        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass


def login():
    clear()
    user = "act"
    passwd = "act"
    username = input("⚡ Username: ")
    password = getpass.getpass(prompt='⚡ Password: ')
    if username != user or password != passwd:
        print("")
        print("⚡ Wrong Password, you're so cute...")
        sys.exit(1)
    elif username == user and password == passwd:
        print("⚡ Welcome to ACT V0.1!")
        time.sleep(0.3)
        ascii_vro()
        main()

login()
