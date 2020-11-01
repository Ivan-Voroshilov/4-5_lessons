from functools import reduce

new_list = [i for i in range(100, 1001) if i % 2 == 0]
fin_list = reduce(lambda a, b: a * b, new_list)
print(fin_list)