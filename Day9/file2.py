import json

data = {
    "name": "Virat",
    "course": "Python",
    "day": 8
}

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)


with open("data.json", "r") as f:
    data = json.load(f)

# Print data
print("Name:", data["name"])
print("Course:", data["course"])
print("Day:", data["day"])