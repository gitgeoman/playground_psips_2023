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
def get_map_of(user: str) -> None:
    city = get_coordinates_of(user['city'])
    map = folium.Map(
        location=city,
        tiles="OpenStreetMap",
        zoom_start=15,
    )
    folium.Marker(
        location=city,
        popup=f'Tu rządzi: {user["name"]},'
              f'postów: {user["posts"]} '
    ).add_to(map)
    map.save(f'mapka_{user["name"]}.html')


def get_map_of(users: list) -> None:
    map = folium.Map(
        location=[52.3, 21.0],
        tiles="OpenStreetMap",
        zoom_start=7,
    )
    for user in users:
        folium.Marker(
            location=get_coordinates_of(city=user['city']),
            popup=f'Użytkownik: {user["name"]} \n'
                  f'Liczba postów {user["posts"]}'
        ).add_to(map)
    map.save('mapka.html')


from dane import users_list

get_map_of(users_list)
