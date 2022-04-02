import requests

word = input("Enter a word to get from the API!: ")
response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
definition = response.json()
definitions = []
print(len(definition[0]['meanings'][0]['definitions']))
if len(definition[0]['meanings'][0]['definitions']) < 5:
    numb = len(definition[0]['meanings'][0]['definitions'])
else:
    numb = 5
for i in range(0, numb):
    definitions.append(definition[0]['meanings'][0]['definitions'][i]['definition'])
print(definitions)
print(len(definitions))
