import requests

API24 = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
takemoney = requests.get(API24)
JsonApi  = takemoney.json()
print(JsonApi)


# takeotherMoney = JsonApi['ccy']['USD']
# print(takeotherMoney)
