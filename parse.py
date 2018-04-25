#!/usr/bin/env python3
import argparse
import datetime
import requests
from bs4 import BeautifulSoup

cinemas = {
            "amersfoort": 23,
            "city": 1,
            "tuschinski": 2,
            "arena": 9,
            "demunt": 10,
            "arnhem": 27,
            "breda": 20,
            "delft": 18,
            "buitenhof": 5,
            "scheveningen": 7,
            "spuimarkt": 13,
            "cinemec_ede": 29,
            "eindhoven": 8,
            "groningen": 4,
            "haarlem": 22,
            "helmond": 11,
            "maastricht": 17,
            "cinemec_nijmegen": 31,
            "dekuip": 12,
            "schouwburgplein": 6,
            "tilburg": 19,
            "rembrandt": 3,
            "zaandam": 14,
            "zwolle": 28,
          }

BASE_URL = "https://en.pathe.nl/cinema/schedules"
# ?cinemaId=9&date=26-04-2018

def parse_movie_html(html):
    movies = {}
    soup = BeautifulSoup(html, 'html.parser')
    for movie in soup.select('.schedule-simple__item'):
        link = movie.select_one('h4 > a')
        title = link.get('title')
        time_slots = []
        for start_time in movie.select('.schedule-time__start'):
            time_slots.append(start_time.text)
        movies[title] = time_slots
    return movies

def get_movies(cinema_id, date):
    r = requests.get(BASE_URL, params={'cinemaId': cinema_id, 'date': date})
    movies = parse_movie_html(r.text)
    return movies

def pretty_print_movies(movies):
    descriptions = []
    for movie_title, time_slots in movies.items():
        if 'Nederlandse' in movie_title:
            continue
        descriptions.append(movie_title)
        descriptions.append("\t" + " ".join(time_slots))

    return '\n'.join(descriptions)

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cinema', type=str, required=True)
    parser.add_argument('--date', type=str, required=True, help="date in format yyyy-mm-dd")
    args = parser.parse_args()
    return (args.cinema, args.date)

def main():
    cinema, date = parse_arguments()
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format")
        exit(1)

    cinema = cinema.lower()
    if cinema not in cinemas:
        print("Cinema not supported! The only cinemas supported are:")
        print("\n".join(cinemas.keys()))
        exit(1)

    cinema_id = cinemas[cinema]
    movie_list = get_movies(cinema_id, date)
    print(pretty_print_movies(movie_list))


if __name__ == '__main__':
    main()
