import webbrowser
import os
import re
import templater


def create_movie_tiles_content(movies):
    """Builds the HTML content for each individual movie item"""
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # fill a movie item with 'this' round of data
        content += templater.fill_template("movie-item",
            {
                "movie_title" : movie.title,
                "poster_image_url" : movie.poster_image_url,
                "trailer_youtube_id" : trailer_youtube_id,
                "storyline" : movie.storyline,
                "rating" : movie.rating
            })
    return content


def open_movies_page(movies):
    """ Builds html page from a list of movies """
    # Create or overwrite the output file
    output_file = open('./fresh_tomatoes.html', 'w')

    # get page content and fill templates for each section
    main_page_head = templater.fill_template("header", {}) # templater.open_template could be used here as well
    rendered_content = ""
    rendered_content = templater.fill_template("body",
        {"movie_tiles" : create_movie_tiles_content(movies)})
    
    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
