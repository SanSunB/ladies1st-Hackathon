from looker import Looker
from worker import Worker


def new_worker(result):
    """ """
    # Get the current id of workers so we can produce unique workers id according to it,
    # by advancing the counter with each worker created
    id_file_name = "id_keeper.txt"
    workers_file_name = "workers.txt"
    Worker.id_counter_initialize(id_file_name)

    print(result['wanted_job'])

    worker1 = Worker(result['current_job'], result['prev_job'], result['degree'])


    # Write the id counter to the file
    Worker.id_counter_final(id_file_name)
