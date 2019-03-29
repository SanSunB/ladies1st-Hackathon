class Worker:
    """ """

    id_counter = None

    def __init__(self):
        """ """
        self.id_number = None
        self.current_job = None
        self.prev_job = None
        self.degree = None

    def __init__(self,current_job, prev_job, degree):
        self.id_number = self.create_id()
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
