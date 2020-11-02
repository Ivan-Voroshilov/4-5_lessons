
file = open('some_text.txt', 'r')
content = file.readlines()
count_lines = 0
word_line_count = 0
word_line = []
for i in content:
    count_lines += 1
    for word in i:
        word_line_count = i.split()
        word_line_count = len(word_line_count)
        word_line.append(word_line_count)
print(f'Количество строк = {count_lines}')
print(f'Количество слов в строках = {set(word_line)}')
file.close()
