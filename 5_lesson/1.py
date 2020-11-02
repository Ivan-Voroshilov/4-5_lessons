
user_input = 'None'
while True:
    if user_input == '':
        break
    user_input = input('Введите строку ')
    with open('text.txt', 'a') as opened_file:
        opened_file.write(f'{user_input}\n')
