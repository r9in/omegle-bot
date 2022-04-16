import requests 
import json
import os
import time
import colorama
from colorama import Fore

os.system("clear")

print(f'''
{Fore.CYAN}
           _                _   _               
          | |              | | (_)              
  __ _  __| |_   _____ _ __| |_ _ ___  ___ _ __ 
 / _` |/ _` \ \ / / _ \ '__| __| / __|/ _ \ '__|
| (_| | (_| |\ V /  __/ |  | |_| \__ \  __/ |   
 \__,_|\__,_| \_/ \___|_|   \__|_|___/\___|_|   
                                                
{Fore.LIGHTRED_EX}[1]{Fore.LIGHTYELLOW_EX} ENGLISH 
{Fore.LIGHTRED_EX}[2]{Fore.LIGHTYELLOW_EX} ITALIAN
{Fore.LIGHTRED_EX}[3]{Fore.LIGHTYELLOW_EX} RUSSIAN
{Fore.LIGHTRED_EX}[4]{Fore.LIGHTYELLOW_EX} GERMAN
{Fore.LIGHTRED_EX}[5]{Fore.LIGHTYELLOW_EX} PORTUGUESE
{Fore.LIGHTRED_EX}[6]{Fore.LIGHTYELLOW_EX} FRENCH
{Fore.LIGHTRED_EX}[7]{Fore.LIGHTYELLOW_EX} INDIAN
{Fore.LIGHTRED_EX}[8]{Fore.LIGHTYELLOW_EX} SPANISH
{Fore.LIGHTRED_EX}[9]{Fore.LIGHTYELLOW_EX} JAPANESE
''')

choice = input(Fore.GREEN+"option => ")

#ENGLISH
if choice == "1":
    message = input("Message => ")
    url = "https://front35.omegle.com/start?caps=recaptcha2,t&firstevents=1&spid=&randid=PL83WE8G&topics=%5B%22friends%22%5D&lang=en"
#ITALIAN
if choice == "2":
    message = input("Message => ")
    url = "https://front35.omegle.com/start?caps=recaptcha2,t&firstevents=1&spid=&randid=PL83WE8G&lang=it"
#RUSSIAN
if choice == "3":
    message = input("Message => ")
    url = "https://front35.omegle.com/start?caps=recaptcha2,t&firstevents=1&spid=&randid=PL83WE8G&lang=ru"
#GERMAN
if choice == "4":
    message = input("Message => ")
    url = "https://front35.omegle.com/start?caps=recaptcha2,t&firstevents=1&spid=&randid=PL83WE8G&lang=de"
#PORTUGUESE
if choice == "5":
    message = input("Message => ")
    url = "https://front35.omegle.com/start?caps=recaptcha2,t&firstevents=1&spid=&randid=PL83WE8G&lang=pt"
#JAPANESE
if choice == "9":
    message = input("Message => ")
    url = "https://front35.omegle.com/start?caps=recaptcha2,t&firstevents=1&spid=&randid=PL83WE8G&lang=ja"

i = 0
while True:
    r = requests.post(url)
    response = r.json()
    print(f'''{Fore.LIGHTRED_EX}[!] - {Fore.CYAN} WAIT! Connecting to stranger...''')
    time.sleep(2)
    print(f'''{Fore.LIGHTRED_EX}[!] - {Fore.LIGHTGREEN_EX} Connected!''')
    
    def omegle(shard):

        global i

        d = {'msg': message, 'id': shard}

        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

        proxies = {
        "http": 'http://144.202.113.237:26381', 
        "http": 'http://192.252.215.5:16137', 
        "http": 'http://65.21.73.217:10003'
        }

        rr = requests.post("https://front44.omegle.com/send", data=d, headers=headers, proxies=proxies)

        if rr.status_code == 200:
            print(Fore.WHITE +"-----------------------------------")
            print(f"YOU: {Fore.CYAN}{message}{Fore.BLUE}")
            print(Fore.WHITE +"-----------------------------------")
        else:
            print(f"failed to send {message}")
        dataa = {'id': shard}
        disconnecting = requests.post("https://front8.omegle.com/disconnect", data=dataa)
        if disconnecting.status_code == 200:
            print(Fore.LIGHTRED_EX+"disconnected")
            time.sleep(2)
            print(Fore.WHITE +"-----------------------------------")
        else:
            print("failed to disconnect")

    def getid():
        shard = response["clientID"]
        if shard.startswith("central"):
            dataa = {'id': shard}
            rrr = requests.post("https://front8.omegle.com/events", data=dataa)
            omegle(shard)
    getid()
