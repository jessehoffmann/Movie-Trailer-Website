"""This file creates a class for the movie trailer website."""
import webbrowser
import urllib


class Movie(object):
    """This class provides a way to store movie related information.

    The class is designed as an outline for storing the data for each
    individual movie. Data includes movie title, storyline, poster image, and
    trailer.

    Attributes:
        VALID_RATINGS (list): List containing possible ratings for each movie.

    Parameters:
        movie_title : str
            Instance for title of the movie.
        movie_storyline : str
            Instance for description of the movie.
        poster_image : str
            Instance for poster image of the movie.
        trailer_youtube : str
            Instance for trailer of the movie.
    """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """The method represents possible instances for movie data."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """The function opens the trailer."""
        webbrowser.open(self.trailer_youtube_url)

    def open_poster(self):
        """The function downloads the poster image."""
        urllib.urlretrieve(self.poster_image_url, "01.jpg")
