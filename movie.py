class Movie(object):

    def __init__(   self, 
                    title=None,
                    duration=None,
                    imdb_id=None,
                    original_title=None,
                    release_date=None,
                    rating="TP",
                    synopsis=None,
                    production_budget=None,
                    marketing_budget=None,
                    actors=None,
                    directors=None,
                    productors=None,
                    is_3d=False,
                    public_note=None,
                    press_note=None
                ):

        self.title = title
        self.duration = duration
        self.imdb_id = imdb_id
        self.original_title = original_title
        self.release_date = release_date
        self.rating = rating
        self.synopsis = synopsis
        self.production_budget = production_budget
        self.marketing_budget = marketing_budget
        self.actors = actors
        self.directors = directors
        self.productors = productors
        self.is_3d = is_3d
        self.public_note = public_note
        self.press_note = press_note


    def total_budget(self):
        if (self.production_budget == None or self.marketing_budget == None):
            return None
        
        return self.production_budget + self.marketing_budget
