import os
import random
import time
import shutil
import logging
import uuid

logging.basicConfig(filename='logfile.txt', level=logging.INFO, 
                    format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


directories = ['./dir1', './dir2', './dir3', './dir4']
for directory in directories:
    if not os.path.exists(directory):
        os.makedirs(directory)
    logging.info(f"Directory created: {directory}")
# Function to randomly create, modify, or delete a file
def random_file_operation(directory):
    random_name = str(uuid.uuid4())
    filename = os.path.join(directory, f"{random_name}.txt")
    operation = random.choice(['create', 'modify', 'delete'])

    if operation == 'create':
        with open(filename, 'w') as f:
            f.write("Hello, World!")
        logging.info(f"File created: {filename}")
    elif operation == 'modify' and os.path.exists(filename):
        with open(filename, 'a') as f:
            f.write("\nModified!")
        logging.info(f"File modified: {filename}")
    elif operation == 'delete' and os.path.exists(filename):
        os.remove(filename)
        logging.info(f"File deleted: {filename}")

    return operation, filename

for _ in range(1000):
    directory = random.choice(directories)
    operation, filename = random_file_operation(directory)
    random_time = random.randint(0,100)

    # Wait a bit for inotify to catch up
    time.sleep(random_time)

    # Read and process events
    


for i in range(1,5):
    path_to_directory = "./dir" + str(i)
    try:
        shutil.rmtree(path_to_directory)
        logging.info(f"Directory removed: {path_to_directory}")
        print(f"The directory {path_to_directory} has been removed")
    except OSError as error:
        logging.info(f"Error removing {path_to_directory}")
        print(f"Error: {error.strerror}. The directory {path_to_directory} was not removed.")
