import requests
import json

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxOGE5YjQwNjM1YmUxYjNjYzZjZjNiMDZkNjI3ODZiNyIsInN1YiI6IjYxMWNhZmE5MWJmODc2MDAyZjk0MmY1YSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.JJY7VlRnSLNqCIXhEGdACd7Ij5d6hBFx5STB2NnN-qY"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

content = get_popular_movies()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

for i in content["results"][:8]:
    print(i)
    
