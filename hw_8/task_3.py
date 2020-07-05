class MyListValueError(Exception):
    def __init__(self, text):
        self.text = text


user_list = []
while True:
    try:
        input_string = input("Input 'stop' to terminate or input number: ")
        if input_string == "stop":
            break
        if not (input_string.replace('.', '', 1).isdigit() or
                (input_string[0] == '-' and input_string[1:].replace('.', '', 1).isdigit())):
            raise MyListValueError("Wrong value in list!")
        else:
            user_list.append(float(input_string))
    except MyListValueError as e:
        print(e)
    else:
        print("Element added!")
print(user_list)
