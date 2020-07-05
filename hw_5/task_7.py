import json

company_to_profit = {}
average_map = {}
profits = []

with open("task_7_input.txt", 'r', encoding='utf-8') as file:
    for line in file:
        company_list = line.split()
        earning = int(company_list[-2])
        costs = int(company_list[-1])
        profits.append(earning - costs)
        company_to_profit[company_list[0]] = profits[-1]

average_map["average"] = sum(profits) / len(profits)
final_list = [company_to_profit, average_map]

with open("task_7_output.json", 'w', encoding='utf-8') as json_file:
    json.dump(final_list, json_file)
