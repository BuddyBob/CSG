import json
from typing import AsyncGenerator
file = open('/Users/aspera/Documents/vscode-ext/CSG/snippets/snippets.code-snippets','w')
dictionary = {}
#----------------------------class with arguments--------------------------------------------------     
for argCount in range(1,20):
    dictionary[f"Class {argCount} args"] = {"prefix":f"csg_a{argCount}","description":f"Class template for {argCount} arguments"}
    classHead = "class ${1:Name}:"
    vars = ', '.join(["${"+str(i+2)+":arg"+str(i+1)+"}" for i in range(argCount)])
    initializer = f"\tdef __init__(self,{vars}):"
    attrs = [f"\t\tself.${i+2} = ${i+2}" for i in range(argCount)]
    dictionary[f"Class {argCount} args"]["body"] = [classHead,initializer]
    for x in attrs:
        dictionary[f"Class {argCount} args"]["body"].append(x)
#----------------------------class with arguments and objects--------------------------------------------------       
for objCount in range(1,20): 
    for argCount in range(1,20):
        title = f"Class {argCount} args {objCount} objects"
        dictionary[title] = {"prefix":f"csg_a{argCount}_o{objCount}","description":f"Class template for {argCount} arguments & {objCount} objects"}
        classHead = "class ${1:Name}:"
        vars = ', '.join(["${"+str(i+2)+":arg"+str(i+1)+"}" for i in range(argCount)])
        initializer = f"\tdef __init__(self,{vars}):"
        attrs = [f"\t\tself.${i+2} = ${i+2}" for i in range(argCount)]
        dictionary[title]["body"] = [classHead,initializer]
        objs = ["${"+str(i+argCount+2)+":obj} = ${1}("+str(vars)+")" for i in range(objCount)]
        #add arguments
        for x in attrs:
            dictionary[title]["body"].append(x)
        #add objects
        for obj in objs:
            dictionary[title]["body"].append(obj)
#----------------------------class with functions--------------------------------------------------        
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
#----------------------------class with functions and objects----------------------------------------------------
for objCount in range(1,20): 
    for funcCount in range(1,20):
        title = f"Class {funcCount} functions {objCount} objects"
        dictionary[title] = {"prefix":f"csg_f{funcCount}_o{objCount}","description":f"Class template for {funcCount} functions & {objCount} objects"}
        classHead = "class ${1:Name}:"
        dictionary[title]["body"] = [classHead]
        functionHeads = ["\tdef ${"+str(i+2)+":func"+str(i+2)+"}(self):"for i in range(funcCount)]
        objs = ["${"+str(i+argCount+2)+":obj} = ${1}()" for i in range(objCount)]
        #add functions
        for head in functionHeads:
            dictionary[title]["body"].append(head)
            dictionary[title]["body"].append("\t\tpass")
        #add objects
        for obj in objs:
            dictionary[title]["body"].append(obj)
#----------------------------class with functions and arguments--------------------------------------------------     
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
#----------------------------class with arguments functions and objects----------------------------------------------------
for objCount in range(1,10): 
    for funcCount in range(1,10):
        for argCount in range(1,20):
            #title
            title = f"Class {argCount} attributes {funcCount} functions {objCount} objects"
            #add description and prefix
            dictionary[title] = {"prefix":f"csg_a{argCount}_f{funcCount}_o{objCount}","description":f"Class template for {argCount} arcuments, {funcCount} functions & {objCount} objects"}
            #class header
            classHead = "class ${1:Name}:"
            #set up arguments
            vars = ', '.join(["${"+str(i+2)+":arg"+str(i+1)+"}" for i in range(argCount)])
            initializer = f"\tdef __init__(self,{vars}):"
            attrs = [f"\t\tself.${i+2} = ${i+2}" for i in range(argCount)]
            dictionary[title]["body"] = [classHead,initializer]
            #function heads
            functionHeads = ["\tdef ${"+str(argCount+i+2)+":func"+str(i+1)+"}(self):"for i in range(funcCount)]
            #objects
            # 1
            # 2
            # 3
            # 4
            # 1
            # 2
            # 3
            # 4
            # 5
            # 1
            # 2   
            objs = ["${"+str(funcCount+argCount+2+i)+":obj} = ${1}("+str(vars)+")" for i in range(objCount)]
            #add attributes
            for x in attrs:
                dictionary[title]["body"].append(x)
            #add functions
            for head in functionHeads:
                dictionary[title]["body"].append(head)
                dictionary[title]["body"].append("\t\tpass")
            #add objects
            for obj in objs:
                dictionary[title]["body"].append(obj)
json.dump(dictionary,file,indent=4)
