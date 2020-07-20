import json

with open("count.json", 'r') as f:
    count = json.load(f)

for word in count:
    print("\"" + word + "\" has been posted " + count[word] + " times."

print()
