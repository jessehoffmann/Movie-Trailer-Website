"""This file creates a class for the movie trailer website."""
import webbrowser
import urllib

class Movie(object):
    """This class provides a way to store movie related information."""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
#        Video.__init__(self, title, duration)
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    def show_trailer(self):
        """This function open the trailer."""
        webbrowser.open(self.trailer_youtube_url)
    def open_poster(self):
        """This function downloads the poster image"""
        urllib.urlretrieve(self.poster_image_url, "01.jpg")
