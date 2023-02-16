import os
from string import ascii_uppercase
from film_player import films_worker


def create_a_z_directories(path):
    os.chdir(path)
    for letter in ascii_uppercase:
        os.mkdir(letter)


create_a_z_directories("film_player/film_storage")

wolf_wall_street = films_worker.Film("The Wolf of Wall Street")
wolf_wall_street.upload_file()
wolf_wall_street.get_film_address()