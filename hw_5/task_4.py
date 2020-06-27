from googletrans import Translator

translator = Translator()

with open("task_4_input.txt", 'r', encoding='utf-8') as read_file:
    with open("task_4_output.txt", 'w', encoding='utf-8') as write_file:
        for line in read_file:
            my_list = line.split()
            my_list[0] = translator.translate(my_list[0], dest='russian').text
            write_file.write(' '.join(my_list) + "\n")
