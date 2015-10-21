"""Creates Movie Instances.

Generates a set of movies as a list of Media objects
"""


import media
import fresh_tomatoes

def addMovie(video_list, video_to_add):
	"""Adds an object to specified list"""
	video_list.append(video_to_add)

#main code
video_list = [];

#init movie
oceans_eleven = media.Media({
	"title" : "Ocean's 11", 
	"trailer_youtube_url" : "https://www.youtube.com/watch?v=imm6OR605UI",
	"storyline" : "A group of 11 men make a plan to rob three vegas casinos.", 
	"poster_image_url" : "./img/poster-image-oceans-eleven.jpg", 
	"rating" : 5
	})
#add to list .. repeat below for the rest of the movies
addMovie(video_list, oceans_eleven)
sharknado = media.Media({
	"title" : "Sharknado", 
	"trailer_youtube_url" : "https://www.youtube.com/watch?v=1hEZkkqjSfs",
	"storyline" : "storyline here", 
	"poster_image_url" : "./img/poster-image-sharknado.jpg", 
	"rating" : 5
	})
addMovie(video_list, sharknado)

#fill template with our data
fresh_tomatoes.open_movies_page(video_list)


