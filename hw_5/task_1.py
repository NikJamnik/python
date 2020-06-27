print("Enter text. Enter '' if you want terminate the program")
with open("task_1_output.txt", 'w') as file:
    input_str = input("Input text: ")
    while input_str != "":
        print(input_str, file=file)
        input_str = input("Input text: ")
