
with open('for_5_task.txt', 'w') as w_obj:
    w_obj.write('1 2 3 4 5 6 7')
with open('for_5_task.txt', 'r') as r_obj:
    for i in r_obj:
        string = i
line = [i for i in string.split()]
summ = 0
for i in line:
    summ += int(i)
print(summ)
