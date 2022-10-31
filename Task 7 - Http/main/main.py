import requests


def get_country_from_ip(ip):
    response = requests.get("http://ip-api.com/json/" + address).json()
    return response.get('country')


address = input("Введите ip-адрес: ")
country = get_country_from_ip(address)

if country == None:
    print("Таĸого IP не существует");
else:
    print(country)
