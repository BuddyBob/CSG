import json
file = open('/Users/aspera/Documents/vscode-ext/CSG/snippets/snippets.code-snippets','w')
dictionary = {}
for argCount in range(1,10):
    dictionary[f"Class {argCount} args"] = {"prefix":f"csg_a{argCount}","description":f"Class template for {argCount} arguments"}
    classHead = "class ${1:Name}:"
    vars = ', '.join(["${"+str(i+2)+":arg"+str(i+1)+"}" for i in range(argCount)])
    initializer = f"\tdef __init__(self,{vars}):"
    attrs = [f"\t\tself.${i+2} = ${i+2}" for i in range(argCount)]
    dictionary[f"Class {argCount} args"]["body"] = [classHead,initializer]
    for x in attrs:
        dictionary[f"Class {argCount} args"]["body"].append(x)
json.dump(dictionary,file,indent=4)
dictionary = {}
for funcCount in range(1,10):
    for argCount in range(1,10):
        funcCount = argCount.copy()
        #title
        title = f"Class {argCount} args {funcCount} functions"
        #set prefix and description
        dictionary[title] = {"prefix":f"csg_a{argCount}_f{funcCount}","description":f"Class template for {argCount} arguments & {funcCount} functions"}
        #class header
        classHead = "class ${1:Name}:"
        #attrivutes
        vars = ', '.join(["${"+str(i+2)+":arg"+str(i+1)+"}" for i in range(argCount)])
        initializer = f"\tdef __init__(self,{vars}):"
        attrs = [f"\t\tself.${i+2} = ${i+2}" for i in range(argCount)]
        #add body to body key
        dictionary[title]["body"] = [classHead,initializer]
        for x in attrs:
            dictionary[title]["body"].append(x)
        functionHeads = ["def {"+str(i+3)+":func}():pass"for i in range(funcCount)]
        for head in functionHeads:
            dictionary[title]["body"].append(head)
        print(functionHeads)
    json.dump(dictionary,file,indent=4)
