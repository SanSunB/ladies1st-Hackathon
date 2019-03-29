from looker import Looker
from worker import Worker


def main():
    """ """
    # Read the Jason file

    # Get the current id of workers so we can produce unique workers id according to it,
    # by advancing the counter with each worker created
    id_file_name = "id_keeper.txt"
    Worker.id_counter_initialize(id_file_name)
    worker1 = Worker()
    worker1.create_id()

    # Write the id counter to the file
    Worker.id_counter_final(id_file_name)


main()
