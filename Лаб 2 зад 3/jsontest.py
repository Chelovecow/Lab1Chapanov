import json

with open('capitals.json') as f:
    dict_user= json.load(f)

print(dict_user)