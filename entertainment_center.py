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

batman_dark_knight = media.Media({
	"title" : "Batman the Dark Knight", 
	"trailer_youtube_url" : "https://www.youtube.com/watch?v=EXeTwQWrcwY",
	"storyline" : "With the help of allies Batman has been able to keep a tight \
		lid on crime in Gotham City. But when the Joker suddenly throws the town \
		into chaos, the caped Crusader begins to tread a fine line between \
		heroism and vigilantism.",
	"poster_image_url" : "./img/poster-image-batman-dark-knight.jpg", 
    "rating" : 4
	})
addMovie(video_list, batman_dark_knight)

atari_game_over = media.Media({
	"title" : "Atari: Game Over", 
	"trailer_youtube_url" : "https://www.youtube.com/watch?v=rIaWAyHIqok",
	"storyline" : "When Atari's game ET massively fails so does the company.\
		Legend states thousands of copies of the ET game were buried underground \
		in a landfill, is ET to blame for the companies downfall?",
	"poster_image_url" : "./img/poster-image-atari-game-over.jpg", 
    "rating" : 2
	})
addMovie(video_list, atari_game_over)

the_town = media.Media({
	"title" : "The Town", 
	"trailer_youtube_url" : "https://www.youtube.com/watch?v=WcXt9aUMbBk",
	"storyline" : "Doug MacRay (Ben Affleck) leads a band of ruthless bank \
		robbers, when he meets a girl he wants to leave the group, this doesnt \
		go over well with the boss.",
	"poster_image_url" : "./img/poster-image-the-town.jpg", 
    "rating" : 4
	})
addMovie(video_list, the_town)

star_wars_four = media.Media({
	"title" : "Star Wars: A New Hope", 
	"trailer_youtube_url" : "https://www.youtube.com/watch?v=1g3_CFmnU7k",
	"storyline" : "The Imperial Forces -- under orders from cruel Darth \
		Vader -- hold Princess Leia hostage, \
		in their efforts to quell the rebellion against the Galactic Empire.",
	"poster_image_url" : "./img/poster-image-star-wars-4.jpg", 
    "rating" : 5
	})
addMovie(video_list, star_wars_four)

ready_player_one = media.Media({
	"title" : "Ready Player One : The Movie", 
	"trailer_youtube_url" : "https://www.youtube.com/watch?v=4ni-9ydZPoA",
	"storyline" : "Welcome to the OASIS, a hyper-realistic, 3D, videogame\
	    paradise. It's 2045, and pretty much everyone logs in to the OASIS \
	 	daily to escape their terrible lives, lives affected by overpopulation,\
	  	unemployment, and energy shortages.",
	"poster_image_url" : "./img/poster-image-ready-player-one.jpg", 
    "rating" : 5
	})
addMovie(video_list, ready_player_one)


#pass our movie list content to be used in page generation
fresh_tomatoes.open_movies_page(video_list)


