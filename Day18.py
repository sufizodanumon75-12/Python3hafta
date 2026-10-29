class Movie:
    def __init__(self, movie_id, title, year, rating):
        self.id = movie_id
        self.title = title
        self.year = year
        self.rating = rating

    def __str__(self):
        return f"""
    ID: {self.id}
    TITLE: {self.title}
    YEAR: {self.year}
    RATING: {self.rating}"""


class MovieManager:
    def __init__(self):
        self.next_id = 1
        self.movies = []

    def create(self, title, year, rating):
        movie = Movie(self.next_id, title, year, rating)
        self.movies.append(movie)
        self.next_id += 1

    def show_all(self):
        for movie in self.movies:
            print(movie)

    def get_by_id(self, movie_id):
        for movie in self.movies:
            if movie.id == movie_id:
                print(movie)
                return

        print("kino nest.")

    def update(self, movie_id, new_title, new_year, new_rating):
        for movie in self.movies:
            if movie.id == movie_id:
                movie.title = new_title
                movie.year = new_year
                movie.rating = new_rating
                return

        print("kino nest.")

    def delete(self, movie_id):
        for movie in self.movies:
            if movie.id == movie_id:
                self.movies.remove(movie)
                return

        print("kino nest.")


manager = MovieManager()


while True:
    print("""
    1. Kino soxtan
    2. Hami kinohora nishon dodan
    3. Kinora ba id yoftan
    4. Obnovit kadan
    5. Udalit kadan
    6. Baromadan
    """)

    choice = int(input("Rakami menura vorid k: "))

    if choice == 1:
        title = input("Nomi kino: ")
        year = int(input("Soli Bromad: "))
        rating = float(input("Reiting kino: "))
        manager.create(title, year, rating)

    if choice == 2:
        manager.show_all()

    if choice == 3:
        movie_id = int(input("Id kinora vorid k: "))
        manager.get_by_id(movie_id)

    if choice == 4:
        movie_id = int(input("Id kinora vorid k: "))
        new_title = input("Nomi navi kinora navis: ")
        new_year = int(input("Nomi soli nav: "))
        new_rating = float(input("Raitingi nav: "))
        manager.update(movie_id, new_title, new_year, new_rating)

    if choice == 5:
        movie_id = int(input("Id kinora vorid k: "))
        manager.delete(movie_id)

    if choice == 6:
        print("Panohton baxdo.")
        break