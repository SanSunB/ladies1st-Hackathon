from looker import Looker
from worker import Worker


def new_worker(result):
    """ """
    # Get the current id of workers so we can produce unique workers id according to it,
    # by advancing the counter with each worker created
    id_file_name = "id_keeper.txt"
    workers_file_name = "workers.txt"
    Worker.id_counter_initialize(id_file_name)

    dict = {'wanted_job':"None", 'current_job':"None", 'prev_job':"None", 'degree':"None"}

    for key, value in result.items():
        if value is not " ":
            dict.update({key:value})


    #looker = Looker("ff","dd", "result['prev_job']", "result['degree']")
    worker = Worker(dict['wanted_job'],dict['current_job'], dict['prev_job'], dict['degree'])

    chosen_worker = worker.get_similar_workers(workers_file_name)


    # Write the id counter to the file
    Worker.id_counter_final(id_file_name)

    return chosen_worker
