class Movie():

    def __init__(   self, 
                    title,
                    duration,
                    imdb_id,
                    original_title=None,
                    release_date=None,
                    rating="TP",
                    plot=None,
                    production_budget=None,
                    marketing_budget=None
                ):

        self.title = title
        self.duration = duration
        self.imdb_id = imdb_id
        self.original_title = original_title
        self.release_date = release_date
        self.rating = rating
        self.plot = plot
        self.production_budget = production_budget
        self.marketing_budget = marketing_budget

        self.id = None
        self.actors = []
        self.productors = []
        self.is_3d = None

    def total_budget(self):
        if (self.production_budget == None or self.marketing_budget == None):
            return None
        
        return self.production_budget + self.marketing_budget
