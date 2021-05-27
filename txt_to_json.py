import os,json

with open("./a") as file:
    lines = file.readlines()
    result = {}
    for l in lines:
        l = l.strip("\n")
        string = l.split("=")
        result[string[0]] = string[1]
with open("./test1.json","w") as file1:
    jas = json.dumps(result)
    file1.write(jas)





