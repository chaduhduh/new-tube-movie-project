class Media:
    """Movie Information Object.

    Class to store information about a single movie, takes 
    param args.

    Attributes: args
    title: String of movie title
    trailer_youtube_url: Url of video trailer
    storyline: String of movie plot
    poster_image_url: Url of video poster image
    rating: An integer of review rating 0-5
    """

    def __init__(self, args):
        """Initializer of Movie"""
        self.title = args["title"]
        self.trailer_youtube_url = args["trailer_youtube_url"]
        self.storyline = args["storyline"]
        self.poster_image_url = args["poster_image_url"]
        self.rating = args["rating"]

