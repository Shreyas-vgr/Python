import media,fresh_tomatoes

toy_story = media.Movie("Toy Story",
			"A story of a boy and his toys that came to life",
			"https://upload.wikipedia.org/wikipedia/en/1/13/Toy_Story.jpg",
			"https://www.youtube.com/watch?v=vwyZH85NQC4")
print(toy_story.storyline)
#toy_story.show_trailer()
movies = [toy_story]
fresh_tomatoes.open_movies_page(movies)
