from worker import Worker


class Looker(Worker):
    """ """
    def __init__(self, wanted_job, industry=None):
        """ """
        self.wanted_job = wanted_job
        self.industry = industry

     def get_similar_workers(self, file):
        f = open(file, "r")
        workers = []
        for x in f:
            worker = x.split("|")
            if (self.wanted_job is worker[1]) or (self.wanted_job is worker[3]):
                workers.append(Worker(worker[0], worker[1], worker[2], worker[3], worker[4]))
        f.close()
        max_match = 0
        match_worker = workers[0]
        for worker in workers:
            curr_match = self.calculate_score(worker)
            if max_match < curr_match:
                match_worker = worker
                max_match = curr_match
        return match_worker, max_match

    def calculate_score(self, worker):
        score = 0
        if self.current_job is worker.job_history:
            score = score + 4
        if self.degree is worker.degree:
            score = score + 3
        if self.job_history is worker.job_history:
            score = score + 2
        if self.courses is worker.courses:
            score = score + 1
        return score
    
        def get_similar_lookers(self, file):
        f = open(file, "r")
        lookers = []
        for x in f:
            looker = x.split("|")
            if self.wanted_job is looker[1]:
                lookers.append(Worker(looker[0], looker[1], looker[2], looker[3], looker[4]))
        f.close()
        return lookers

