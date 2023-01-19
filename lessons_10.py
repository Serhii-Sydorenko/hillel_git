##4 задание
exercise_4 = lambda movie: movie.get("rating")
rank = 8.5
filtered_movies = [movie for movie in imdb_rank if float(movie.get("rating")) > rank]
sorted(filtered_movies, key=lambda movie: movie.get("rating"))
[print(movie) for movie in filtered_movies]

##5 задание
def exercise_6(person, all_movies):
    results = {"name": person, "amount": 0, "movies": []}
    for movie in all_movies:
        if person in movie.get("director") or [w for w in movie.get("writers") if person in w]:
            results["amount"] += 1
            movie_info = {"title": movie.get("title"),
                          "rating": movie.get("rating")}
            results["movies"].append(movie_info)
    return results

##6 задание
workers = ["Sergio Leone", "Peter Jackson", "Hayao Miyazaki", "Betty Comden", "NotExistedName"]
for writer_or_director in workers:
    results_4 = exercise_6(writer_or_director, imdb_rank)
    print(results_4)
