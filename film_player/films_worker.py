class Film():
    def __init__(self, name, rating, year, directed, starring):
        self.name = name
        self.rating = rating
        self.year = year
        self.directed = directed
        self.starring = starring
        self.storage_address = 'адрес'
    def film_info(self):
        info = ("Film name is: " + self.name + ". Current rating is: " + self.rating + ". Directed on: " + self.directed + " in " + str(self.year) + ". Starring: " + self.starring).title()
        print(info)
    def upload_file(self):
        import os
        import string

        for c in string.ascii_uppercase:
            os.chdir("D:/Users/dn300990ssk/PycharmProjects/hillel_git/film_player/film_storage")
            if c == self.name[0]:
                os.chdir("D:/Users/dn300990ssk/PycharmProjects/hillel_git/film_player/film_storage"+str(c))
                file = open(self.name+'.txt','w')

    def get_film_address(self):
        import os
        address = os.path.abspath(self.name+'.txt')
        self.storage_address = address
        print(self.storage_address)


my_favorite_film = Film("Titanic", "7.8 / 10", 1997, "James Cameron", "Leonardo DiCaprio, Kate Winslet, and Billy Zane")

#информация
my_film.film_info()

#upload_file - створює txt файл зназвою фільму
my_film.upload_file()

#get_film_address повертає повний шлях(hzljr) до фільму у дериктроії.
my_film.get_film_address()