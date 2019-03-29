class Worker:
    """ """

    id_counter = None

    def __init__(self):
        """ """
        self.id_number = None
        self.wanted_job = None
        self.current_job = None
        self.prev_job = None
        self.degree = None

    def __init__(self,wanted_job=None, current_job=None, prev_job=None, degree=None):
        self.id_number = self.create_id()
        self.wanted_job = wanted_job
        self.current_job = current_job
        self.prev_job = prev_job
        self.degree = degree

    def create_id(self):
        """ advance the worker id and keep it in teh file """
        Worker.id_counter += 1
        return Worker.id_counter

    def read_worker_from_file(self):
        """ """
        pass

    def create_worker_jason(self):
        """ """
        pass

    def write_worker_to_file(self):
        """ """
        pass

    @staticmethod  # Define the method as static
    def id_counter_initialize(file_name):
        """ Initialize the current counter of the workers id's"""
        # Open the id file in read mode
        fr = open(file_name, 'r')

        # Get the id from the file
        id_current = fr.read()

        # initialize the global worker id variable
        Worker.id_counter = int(id_current)

        fr.close()

    @staticmethod  # Define the method as static
    def id_counter_final(file_name):
        """ Initialize the current counter of the workers id's"""
        # Open the id file in read mode
        fw = open(file_name, 'w')

        # write the worker id to the file
        fw.write(str(Worker.id_counter))

        fw.close()

    def get_similar_workers(self, file):
        f = open(file, "r")
        workers = []
        gb =[]
        for x in f:
            worker = x.split("|")
            if (self.wanted_job == worker[1]) or (self.wanted_job == worker[3]):
                #print(worker[0], worker[1], worker[2], worker[3], worker[4])
                #workers.append(Worker(worker[1], worker[2], worker[3], worker[4]))
                gb =[worker[1], worker[2], worker[3], worker[4]]
                break
        f.close()
        max_match = 0
        if len(workers) > 0:
            match_worker = workers[0]
            for worker in workers:
                curr_match = self.calculate_score(worker)
                if max_match < curr_match:
                    match_worker = worker
                    max_match = curr_match
        gb.append(max_match)
        return gb

    def calculate_score(self, worker):
        score = 0
        if self.current_job is worker.prev_job:
            score = score + 4
        if self.degree is worker.degree:
            score = score + 3
        if self.prev_job is worker.prev_job:
            score = score + 2
        return score
