from flask import Flask, render_template
from random import randint, randrange

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def homepage():
    movies = generate_movies()
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
