import openpyxl
import json

wb = openpyxl.load_workbook('two.xlsx')
sheet = wb.active

items = sheet['A2':'B6']

# convert

dict_nums = dict()
for rows in items :
    key = rows[0].value
    value = rows[1].value
    dict_nums[key] = value
    
print(dict_nums)

json_dump = json.dumps(dict_nums)

print(json_dump)

json_file = open('test.json', 'w')
json.dump(dict_nums, json_file)
json_file.close()