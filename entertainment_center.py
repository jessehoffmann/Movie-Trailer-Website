import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life.",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=v-PjgYDrg70")
#print(toy_story.storyline)
avatar = media.Movie("Avatar", "Humans visit an alien world in an attempt to steal the planet's resources.",
                    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=d1_JBMrrYw8")
#avatar.show_trailer()
good_will_hunting = media.Movie("Good Will Hunting", "A young genius struggles to find his place in the world.",
                                "https://upload.wikimedia.org/wikipedia/en/5/52/Good_Will_Hunting.png",
                                "https://www.youtube.com/watch?v=PaZVjZEFkRs")
#good_will_hunting.show_trailer()
blue_is_the_warmest_color = media.Movie("Blue Is The Warmest Color", "A Frech teen forms a deep emotional bond with an older art student",
                                        "https://upload.wikimedia.org/wikipedia/en/3/3e/La_Vie_d%27Ad%C3%A8le_film_poster.png",
                                        "https://www.youtube.com/watch?v=Y2OLRrocn3s")
kung_fu_panda = media.Movie("Kung Fu Panda", "A panda learns kung fu in the hopes of saving his town.",
                            "https://upload.wikimedia.org/wikipedia/en/7/76/Kungfupanda.jpg",
                            "https://www.youtube.com/watch?v=PXi3Mv6KMzY")
oneeighty_degrees_south = media.Movie("180 Degrees South", "A man travels to South America for the journey of a lifetime.",
                                    "https://upload.wikimedia.org/wikipedia/en/7/70/180_South.jpg",
                                    "https://www.youtube.com/watch?v=NK3TOHLFL50")
movies = [toy_story, avatar, good_will_hunting, blue_is_the_warmest_color, kung_fu_panda, oneeighty_degrees_south]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
