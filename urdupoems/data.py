import json

# Open the JSON file for reading
with open('poems_data.json', 'r', encoding='utf-8') as file:
    # Load the JSON data
    data = json.load(file)

# Now you can work with the loaded JSON data
# print(data)
print(len(data))

# for poem in data:
#     print(poem['poet_name'])
#     print(poem['poem_name'])
#     print(poem['poem_lines'])
