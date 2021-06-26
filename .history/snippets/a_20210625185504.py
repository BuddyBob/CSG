import json
file = open('/Users/aspera/Documents/vscode-ext/CSG/snippets/snippets.code-snippets','w')
dictionary = {}
for argCount in range(1,20):
    dictionary[f"Class {argCount} args"] = {"prefix":f"csg_a{argCount}","description":f"Class template for {argCount} arguments"}
    classHead = "class ${1:Name}:"
    vars = ', '.join(["${"+str(i+2)+":arg"+str(i+1)+"}" for i in range(argCount)])
    initializer = f"\tdef __init__(self,{vars}):"
    attrs = [f"\t\tself.${i+2} = ${i+2}" for i in range(argCount)]
    dictionary[f"Class {argCount} args"]["body"] = [classHead,initializer]
    for x in attrs:
        dictionary[f"Class {argCount} args"]["body"].append(x)
for funcCount in range(1,20):
    #title
    title = f"Class {funcCount} functions"
    #title, prefix description added
    dictionary[title] = {"prefix":f"csg_f{funcCount}","description":f"Class template for {funcCount} functions"}
    #class head
    classHead = "class ${1:Name}:"
    dictionary[title]["body"] = [classHead]
    #function heads added
    functionHeads = ["\tdef ${"+str(i+2)+":func"+str(i+2)+"}(self):"for i in range(funcCount)]
    for head in functionHeads:
        dictionary[title]["body"].append(head)
        dictionary[title]["body"].append("\t\tpass")
for funcCount in range(1,20):
    for argCount in range(1,30):
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
        functionHeads = ["\tdef ${"+str(argCount+i+2)+":func"+str(i+1)+"}(self):"for i in range(funcCount)]
        for head in functionHeads:
            dictionary[title]["body"].append(head)
            dictionary[title]["body"].append("\t\tpass")
json.dump(dictionary,file,indent=4)
