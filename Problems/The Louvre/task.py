class Painting:
    museum = "Louvre"

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year

    def printing_(self):
        print(f'"{self.title}" by {self.artist} ({self.year}) hangs in the {Painting.museum}.')


Painting(input(), input(), input()).printing_()
