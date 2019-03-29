from worker import Worker


class Looker(Worker):
    """ """
    def __init__(self, wanted_job, industry=None):
        """ """
        self.wanted_job = wanted_job
        self.industry = industry

    def get_similar_workers(self):
        """ """
        pass
