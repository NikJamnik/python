less_than_20 = []
salaries = []

with open("task_3_input.txt", 'r', encoding='utf-8') as file:
    for line in file:
        person, salary = line.split()
        salaries.append(float(salary))
        if salaries[-1] < 20000:
            less_than_20.append((person, salaries[-1]))

print(f"Average salary: {sum(salaries) / len(salaries):.2f}")
print(f"Less than 20K: {less_than_20}")
