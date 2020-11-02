
import json

with open('for_7_task.txt', 'r') as r_obj:
    firms_dict = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in r_obj}
summ = 0
for item in firms_dict:
    summ += firms_dict[item]
# print(firms_dict)
with open('for_7_task.txt', 'r') as r_obj:
    count_lines = 0
    for i in r_obj.readlines():
        count_lines += 1
aver_dict = {'average': summ / count_lines}
# print(aver_dict)
final_list = [firms_dict, aver_dict]
print(final_list)
with open('7_task_file.json', 'w') as w_obj:
    json.dump(final_list, w_obj)
