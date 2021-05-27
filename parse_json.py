import os,json

with open('test1.json','r') as jsonfile:
    json_string = json.load(jsonfile)

print(json_string['IP'])
print(json_string['hostname'])
print(json_string['usercpu'])
print(json_string['freecpu'])
print(json_string['cputexttime'])
print(json_string['osreaminmem'])
