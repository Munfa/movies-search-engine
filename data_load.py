import requests
import json
from time import sleep

API_key = "TMDB_API"
base_url = "https://api.themoviedb.org/3"
total_pages = 5
start_year = 2000
end_year = 2025

def load_movies(page, year):
    url = f"{base_url}/discover/movie"
    params = {
        "api_key": API_key,
        "vote_count.gte": 100,
        "vote_average.gte": 6.5,
        "with_original_language": "en",
        "primary_release_year": year,
        "page": page
    }

    r = requests.get(url, params=params)
    r.raise_for_status()
    return r.json().get("results", [])

def get_genre_map():
    url = f"{base_url}/genre/movie/list?api_key={API_key}&language=en-US"
    res = requests.get(url).json()
    return {genre["id"]: genre["name"] for genre in res["genres"]}

def get_movies():
    genre_map = get_genre_map()
    all_movies = []
    for year in range(start_year, end_year+1):
        for page in range(1, total_pages+1):
            movies = load_movies(page, year)
            if not movies:
                break
            for m in movies:
                movie_data = {
                    "title": m.get("title"),
                    "overview": m.get("overview"),
                    "rating": m.get("vote_average"),
                    "release_date": m.get("release_date"),
                    "genre": [genre_map[g] for g in m.get("genre_ids", [])],
                    "poster_url": f"https://image.tmdb.org/t/p/w500{m.get('poster_path')}" if m.get("poster_path") else None
                }
                all_movies.append(movie_data)
        
        sleep(0.50)
    with open("movies.json", 'w', encoding='utf-8') as file:
        json.dump(all_movies, file, indent=4)