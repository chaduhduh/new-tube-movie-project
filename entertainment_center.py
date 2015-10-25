"""Creates Movie Instances.

Stores a set of movies as a list of Media objects to
display in a web page.
"""


import media
import fresh_tomatoes

def addMovie(video_list, video_to_add):
	"""Adds an object to specified list"""
	video_list.append(video_to_add)

#start main code
video_list = [];

#init movie
oceans_eleven = media.Media({
	"title" : "Ocean's 11", 
	"trailer_youtube_url" : "https://www.youtube.com/watch?v=imm6OR605UI",
	"storyline" : "A group of 11 men make a plan to rob three vegas casinos.", 
	"poster_image_url" : "./img/poster-image-oceans-eleven.jpg", 
	"rating" : 5
	})
#add to list video list
addMovie(video_list, oceans_eleven)

#repeat below for the rest of the movies
sharknado = media.Media({
	"title" : "Sharknado", 
	"trailer_youtube_url" : "https://www.youtube.com/watch?v=1hEZkkqjSfs",
	"storyline" : "Tornados filled with sharks... Enough Said!", 
	"poster_image_url" : "./img/poster-image-sharknado.jpg", 
	"rating" : 2
	})
addMovie(video_list, sharknado)

dumb_and_dumber = media.Media({
	"title" : "Dumb and Dumber", 
	"trailer_youtube_url" : "https://www.youtube.com/watch?v=l13yPhimE3o",
	"storyline" : "Two friends travel across the country to deliver a lost suit\
	    case to a women. Jim Carrey and Jeff Daniels star in this comedy.",
	"poster_image_url" : "./img/poster-image-dumb-and-dumber.jpg", 
	"rating" : 5
	})
addMovie(video_list, dumb_and_dumber)

#pass our movie list content to be used in page generation
fresh_tomatoes.open_movies_page(video_list)


