import requests
import bs4


def get_weather():
    response = requests.get("https://yandex.ru/pogoda")
    tree = bs4.BeautifulSoup(response.text, 'html.parser')

    for item in tree.select('.forecast-briefly__day-link')[1:9]:
        print(item.attrs['aria-label'])


get_weather()