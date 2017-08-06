import webbrowser

class Movie():
	"""This class provides a way to movie related information"""
	# VALID_RATINGS = ["G", "PG", "PG-13", "R"]
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		# The constructor takes these following parameters that defines the object in file "entertainment_center.py"
		self.title = movie_title						# defines Title of the movie
		self.storyline = movie_storyline				# defines Movie basic storyline
		self.poster_image_url = poster_image 			# defines URL of the Movie Poster
		self.trailer_youtube_url = trailer_youtube 		# defines URL of the Youtube 

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)		# defines "Viewing Trailer of the movie in Browser"