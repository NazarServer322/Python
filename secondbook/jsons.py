import json
StringJsonData = '{ "name": "Nazar", "Age": "25", "population":"Human" }'

JsonValue = json.loads(StringJsonData)
print(JsonValue)



PythonInJson = {'Name':'Nazar', 'Age': '25'}
TransleteInJson = json.dumps(PythonInJson)
print(TransleteInJson)