from random import randint

my_list = [randint(0, 101) for _ in range(100)]
with open("task_5_output.txt", 'w+', encoding='utf-8') as file:
    for el in my_list:
        file.write(str(el) + " ")
    file.seek(0)
    my_sum = sum(map(int, file.readlines()[0].split()))

print(f"Sum: {my_sum}")
