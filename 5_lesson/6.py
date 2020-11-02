
def f_sum(a, b, c):
    return int(a) + int(b) + int(c)


with open('for_6_task.txt', 'r') as r_obj:
    obj_dict = {line.split()[0]: f_sum(line.split()[1], line.split()[2], line.split()[3]) for line in r_obj}
print(obj_dict)
