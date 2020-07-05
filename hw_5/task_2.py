file_name = "task_1_output.txt"
line_counter = 0

with open(file_name, 'r', encoding='utf-8') as file:
    for i, line in enumerate(file):
        line_counter += 1
        my_list = line.split()
        print(f"Line {i + 1}: {len(my_list)} words")
print(f"Total count of lines: {line_counter}")
