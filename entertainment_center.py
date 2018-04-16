"""This file creates objects for the specific movies."""
import media
import fresh_tomatoes

A_QUIET_PLACE = media.Movie("A Quiet Place", "In a post-apocalyptic world a " \
                            "family tries to survive without making a sound.",
                            "https://upload.wikimedia.org/wikipedia/en/a/a0/" \
                            "A_Quiet_Place_film_poster.png",
                            "https://www.youtube.com/watch?v=WR7cc5t7tv8")
#print(toy_story.storyline)
AVATAR = media.Movie("Avatar", "Humans visit an alien world in an attempt to" \
                     "steal the planet's resources.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/"\
                     "Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")
#avatar.show_trailer()
GOOD_WILL_HUNTING = media.Movie("Good Will Hunting", "A young genius struggles"
                                "to find his place in the world.",
                                "https://upload.wikimedia.org/wikipedia/en/5/"\
                                "52/Good_Will_Hunting.png",
                                "https://www.youtube.com/watch?v=PaZVjZEFkRs")
#good_will_hunting.show_trailer()
BLUE_IS_THE_WARMEST_COLOR = media.Movie("Blue Is The Warmest Color",
                                        "A Frech teen forms a deep emotional"\
                                        " bond with an older art student",
                                        "https://upload.wikimedia.org/"\
                                        "wikipedia/en/3/3e/La_Vie_d%27Ad%C3%A"\
                                        "8le_film_poster.png",
                                        "https://www.youtube.com/watch?v=Y2"\
                                        "OLRrocn3s")
KUNG_FU_PANDA = media.Movie("Kung Fu Panda", "A panda learns kung fu in the"\
                            "hopes of saving his town.",
                            "https://upload.wikimedia.org/wikipedia/en/7/76/"\
                            "Kungfupanda.jpg",
                            "https://www.youtube.com/watch?v=PXi3Mv6KMzY")
ONEEIGHTY_DEGREE_SOUTH = media.Movie("180 Degrees South", "A man travels to"\
                                     "South America for the journey of a "\
                                     "lifetime.",
                                     "https://upload.wikimedia.org/wikipedia"\
                                     "/en/7/70/180_South.jpg",
                                     "https://www.youtube.com/watch?v=NK3TOH"\
                                     "LFL50")
MOVIES = [A_QUIET_PLACE, AVATAR, GOOD_WILL_HUNTING, BLUE_IS_THE_WARMEST_COLOR,
          KUNG_FU_PANDA, ONEEIGHTY_DEGREE_SOUTH]
fresh_tomatoes.open_movies_page(MOVIES)
