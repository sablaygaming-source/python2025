
def fDispDict(pDict, pPrompt ): #2
    print(pPrompt)
    for i, (k, v )in enumerate(pDict.items()): #3

        print(f"\n{i} = {k} : {v}", end= "")
    #3
    print()
#2

def fShowType(pDict, pPrompt): #2
    print(pPrompt)
    for k, v in pDict.items():#3

        print(f"\n{k}:{type(v).__name__}")
    #3
    print( )
#2

vName = "NAME"
vValue = "Ando"
vDict = { "ID": 1, vName: vValue, "EMAIL": "Ando@email"} 

fDispDict( vDict, f"\ndisplays the value of vDict")

vDict[vName ] = "bentong"

fDispDict( vDict, f"\ndisplays the value of vDict edited ")

print(f"{vName=}, {vValue=}")

vDict["DELETEME"] = "delete1"

fDispDict( vDict, f"\ndisplays the value of vDict edited2 ")

keys = list( vDict.keys())

print(f"\n{keys= }")

vDict.pop(keys[3])

vDict["deleteme"] = "nabura na"

#update the keys for index purpose
keys = list( vDict.keys())

fDispDict( vDict, f"\ndisplays the value of vDict edited3 ")

lowerDict = {  k.lower() : ( v if isinstance( v, int) else v.lower() )  for k, v in vDict.items() }

fShowType(lowerDict, "\nshowing the type")

print("\nend of prog")
