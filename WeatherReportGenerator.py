import requests

url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

resp = requests.get(url, verify=False)

listWeathers = resp.json()['list']


def get_Weather(date_inp):
    for i in listWeathers:
        if date_inp in i['dt_txt']:
            return i
    return False


choice = 1

while choice != "0":
    print("1 for weather")
    print("2 for Wind Speed")
    print("3 for Pressure")
    print("0 for Exit")
    choice = input("Enter a choice")
    if choice == "1":
        date = input("Enter date in format(YYYY-MM-DD hh-mm-ss) :")
        result = get_Weather(date)
        if result != 0:
            print("Main: " + result['weather'][0]['main'])
            print("Description " + result['weather'][0]['description'])
    elif choice == "2":
        date = input("Enter date in format(YYYY-MM-DD hh-mm-ss) :")
        result = get_Weather(date)
        if result != 0:
            print("Wind speed: " + str(result['wind']['speed']))
    elif choice == "3":
        date = input("Enter date in format(YYYY-MM-DD hh-mm-ss) :")
        result = get_Weather(date)
        if result != 0:
            print("Pressure: " + str(result['main']['pressure']))