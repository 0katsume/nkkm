import os
import time
import requests
from fake_useragent import UserAgent
from termcolor import colored


def request(name, url, name_phone, phn, sec):
    headers = {'user-agent': UserAgent().random}

    try:
        requests.post(url, headers=headers, data={name_phone: phn})
        print(f'{colored("[+]", "green")} {name} отправлено')
    except:
        print(f'{colored("[-]", "red")} {name} не отправлено')

    time.sleep(sec)


def menu():
    print('''
[1] SMS Bomber
[2] About

[0] Exit''')


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
