subject_to_hours = {}

with open("task_6_input.txt", 'r', encoding='utf-8') as file:
    for line in file:
        name, digit_string = line.split(':')
        digit_list = digit_string.split()
        subject_sum = 0
        for el in digit_list:
            if '(' in el:
                number, _ = el.split('(')
                subject_sum += int(number)
        subject_to_hours[name] = subject_sum

print(f"Subject and their hours: {subject_to_hours}")
