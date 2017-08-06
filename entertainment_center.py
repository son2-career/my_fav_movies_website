### PLEASE NOTE TO KEEP "entertainment_center.py", "fresh_tomato.py" & "media.py" in same directory for working of the project.

import fresh_tomato 	# imports the website design using fresh_tomato.py
import media		# imports media.py where the class file is defined

# List of Movies as objects of class in media.py are as follows with their variables:

dalgal = media.Movie("Dangal",
						"Story abount a man of making Daughter's career in Wrestling",
						"https://upload.wikimedia.org/wikipedia/en/9/99/Dangal_Poster.jpg",
						"https://www.youtube.com/watch?v=x_7YlGv9u1g")

a_wednesday = media.Movie("A Wednesday", 
						"Story of a common-man's fight against Terrorism",
						"https://upload.wikimedia.org/wikipedia/en/thumb/7/77/A_Wednesday_Poster.JPG/220px-A_Wednesday_Poster.JPG",
						"https://www.youtube.com/watch?v=LGfwASavWNQ")

titanic = media.Movie("Titanic", 
						"A love story in the the Great ship, Titanic",
						"https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",
						"https://www.youtube.com/watch?v=2e-eXJ6HgkQ")

three_idiots = media.Movie("3 idiots", 
						"Story of 3 Engg. College friends about their life",
						"https://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg",
						"https://www.youtube.com/watch?v=2lK31lpyrkU")

swades = media.Movie("Swades", 
						"Story of a Indian NASA scientist returning back to India",
						"https://upload.wikimedia.org/wikipedia/en/8/85/Swades_poster.jpg",
						"https://www.youtube.com/watch?v=sKVkvv_i-3o")

taare_zameen_par = media.Movie("Taare Zameen Par", 
						"Story of a child, facing problem of dyslexia",
						"https://upload.wikimedia.org/wikipedia/en/b/b4/Taare_Zameen_Par_Like_Stars_on_Earth_poster.png",
						"https://www.youtube.com/watch?v=qLsiGq-aC88")


movies = [dalgal, a_wednesday, titanic, three_idiots, swades, taare_zameen_par]  	# List of movies' variable
fresh_tomato.open_movies_page(movies) 							# Open the Processed Website


