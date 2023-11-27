#### BEAUTIFULSOUP4

from bs4 import BeautifulSoup
import requests
import folium

# -*- coding: utf-8 -*-

nazwy_miejscowości = ['Opoczno', 'Lublin', 'Gdańsk']


def get_coordinates_of(city: str) -> list[float, float]:
    # pobranie strony internetowe
    adres_URL = f'https://pl.wikipedia.org/wiki/{city}'
    response = requests.get(url=adres_URL)
    response_html = BeautifulSoup(response.text, 'html.parser')

    # pobranie współrzędnych z treści strony internetowej
    response_html_latitude = response_html.select('.latitude')[1].text  # .  class
    response_html_latitude = float(response_html_latitude.replace(',', '.'))
    response_html_longitude = response_html.select('.longitude')[1].text  # .  class
    response_html_longitude = float(response_html_longitude.replace(',', '.'))

    return [response_html_latitude, response_html_longitude]

# for item in nazwy_miejscowości:
#     print(get_coordinates_of(item))


# zwrócić mape z pinezką odnoszącą się do użytkownika podanego z klawiatury
# zwróci mapę z wszystkimi użytkownikami z danej listy (znajomymy)

### RYSOWANIE MAPY

city= get_coordinates_of(city='Zamość')
map = folium.Map(
    location=[52.3, 21.0],
    tiles="OpenStreetMap",
    zoom_start=7,
    )
for item in nazwy_miejscowości:
    folium.Marker(
        location=get_coordinates_of(city=item),
        popup='GEOINFORMATYKA RZĄDZI OU YEEEEEAAAAH!\n🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀'
    ).add_to(map)
map.save('mapka.html')














