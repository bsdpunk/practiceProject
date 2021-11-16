import json
 
# Opening JSON file
f = open('countries.json',)
 
# returns JSON object as
# a dictionary
data = json.load(f)
 
# Iterating through the json
# list
#for i in data:
#    print(i)
aList = json.dumps(data)
# Closing file
print(aList)
#aDict = json.loads(str(data))

f.close()
