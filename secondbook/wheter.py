import requests
import json
import sys
from supersicretappi import api

def weather(City):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={City}&appid={api}"
    getwetherfromappi = requests.get(url)
    test = getwetherfromappi.json()
    tempcity = ((test['main']['temp']) -273.15)
    today = test['weather'][0]['description']
    inInt = int(tempcity)
    if  inInt < 0:
        print("it's cold as ppc")
    elif inInt in range (1,19):
        print("please wear warm clonthes")
    elif inInt > 20:
        print("Nice it's sunny today")
    else:        
        print("try")
    print(inInt)  
    print(today)
Enter = input("Enter your City: ")
weather(Enter)



