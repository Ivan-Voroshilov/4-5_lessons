
text_out = open('4_task_result.txt', 'a')
text = open('for_4_task.txt', 'r')
text_part = text.readline()[-4:]
text_out.write(f'odin {text_part}\n')
text_part = text.readline()[-4:]
text_out.write(f'dva {text_part}\n')
text_part = text.readline()[-4:]
text_out.write(f'tri {text_part}\n')
text_part = text.readline()[-3:]
text_out.write(f'chetyre {text_part}\n')
