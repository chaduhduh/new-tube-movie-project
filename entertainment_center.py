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

beverly_hills_ninja = media.Media({
	"title" : "Beverlly Hills Ninja", 
	"trailer_youtube_url" : "https://www.youtube.com/watch?v=L7wjZZDmyhY",
	"storyline" : "The story of the legendary white ninja. Is Hary really the \
		white ninja? .. some say it is so.",
	"poster_image_url" : "./img/poster-image-beverly-hills-ninja.jpg", 
    "rating" : 5
	})
addMovie(video_list, beverly_hills_ninja)

tommy_boy = media.Media({
	"title" : "Tommy Boy", 
	"trailer_youtube_url" : "https://www.youtube.com/watch?v=6nQ4K2bvVxY",
	"storyline" : "After his dad's death, it is up to Tommy (Chris Farley) to\
		save the future of his company.",
	"poster_image_url" : "./img/poster-image-tommy-boy.jpg", 
    "rating" : 5
	})
addMovie(video_list, tommy_boy)

catch_me_if_you_can = media.Media({
	"title" : "Catch Me if You Can", 
	"trailer_youtube_url" : "https://www.youtube.com/watch?v=hFj3OXVL_wQ",
	"storyline" : "After his parents divorce, a kid undertakes check fraud as \
		a means to survive. Will one cops obsession laed to this boys arrest?",
	"poster_image_url" : "./img/poster-image-catch-me-if-you-can.jpg", 
    "rating" : 4
	})
addMovie(video_list, catch_me_if_you_can)



#pass our movie list content to be used in page generation
fresh_tomatoes.open_movies_page(video_list)


