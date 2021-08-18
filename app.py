from tmdb_client import get_popular_movies, get_poster_url
from flask import Flask, render_template

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}

@app.route('/')
def homepage():
    movies = get_popular_movies()["results"][:8]
    return render_template("homepage.html", movies=movies)


class Film:
    def __init__ (self, tytul, rok_wydania, gatunek, liczba_odtworzen):
        self.tytul=tytul
        self.rok_wydania=rok_wydania
        self.gatunek=gatunek
        self.liczba_odtworzen = liczba_odtworzen

    def __str__ (self):
        return f'{self.tytul} {self.rok_wydania} {self.gatunek} {self.liczba_odtworzen}'


id_movie = Film (tytul='Niemozliwe', rok_wydania ='2015', gatunek ='katastroficzny', liczba_odtworzen = 6)

def generate_movies():
    movies_all = []
    for i in range(10):
        movies_all.append(id_movie)
    return movies_all

test = generate_movies()
for i in test:
    print(i.tytul)


testing_pop_movies = get_popular_movies