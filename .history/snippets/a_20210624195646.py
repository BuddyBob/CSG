import json
file = open('/Users/aspera/Documents/vscode-ext/CSG/snippets/snippets.code-snippets','w')
dictionary = {}
for argCount in range(1,10):
    dictionary[f"Class {argCount} args"] = {"prefix":f"csg{argCount}","description":f"Class template for {argCount} arguments"}
    classHead = "class ${1:Name}"
    vars = ', '.join(["${"+str(i+2)+":arg"+str(i+1)+"}" for i in range(argCount)])
    initializer = f"\tdef __init__(self,{vars})"
    attrs = [f"\t\tself.${i+2} = ${i+2}" for i in range(argCount)]
    dictionary[f"Class {argCount} args"]["body"] = [classHead,initializer]
    for x in attrs:
        dictionary[f"Class {argCount} args"]["body"].append(x)
json.dump(dictionary,file,indent=4)