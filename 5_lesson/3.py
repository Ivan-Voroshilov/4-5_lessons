
file = open('names.txt', 'r')
file_dict = {line.split()[0]: line.split()[1] for line in file}
# print(file_dict)
low_payments = []
all_pay = []
for i in file_dict:
    all_pay.append(int(file_dict[i]))
    if int(file_dict[i]) < 20000:
        low_payments.append(i)
print(f'Зарплата менее 20000 у: {low_payments}')
print(f'Средняя зарплата = {sum(all_pay) / len(all_pay)}')
