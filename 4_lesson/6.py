
def first_scr(start):
    from itertools import count
    new_list = []
    for i in count(int(start)):
        if i > 10:
            break
        new_list.append(i)
    return new_list


def second_scr():
    from itertools import cycle
    def_list = [1, 2, 3]
    count = 0
    new_list = []
    for i in cycle(def_list):
        if count > 9:
            break
        new_list.append(i)
        count += 1
    return new_list


print(first_scr(3))
print(second_scr())
