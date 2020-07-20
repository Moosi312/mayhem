import json

with open("count.json", 'r') as f:
    count = json.load(f)

print()
print("Posted words:")
for word in count:
    print("\t\"" + word + "\" has been posted " + str(count[word]) + " times.")
          
print()
