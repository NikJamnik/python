class MyZeroDivisionError(Exception):
    def __init__(self, text):
        self.text = text


try:
    dividend, divisor = map(int, input("Input dividend and divisor separated by ' ': ").split())
    if divisor == 0:
        raise MyZeroDivisionError("MyZeroDivisionError! Divisor can't be 0!")
except ValueError:
    print("ValueError! Numbers must be integers!")
except MyZeroDivisionError as e:
    print(e)
else:
    print(f"Division result = {dividend / divisor}")
finally:
    print("Session is completed!")
