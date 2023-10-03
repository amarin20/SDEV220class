import multiprocessing
import random
import time
from datetime import datetime

def process_function():
    # Generate a random sleep time between 0 and 1 second
    sleep_time = random.uniform(0, 1)
    time.sleep(sleep_time)
    current_time = datetime.now()   
    print(f"Process ID {multiprocessing.current_process().pid}: Current Time - {current_time}")

if __name__ == "__main__":
    # Create three separate processes
    processes = [multiprocessing.Process(target=process_function) for _ in range(3)] 
    for process in processes:
        process.start()
    for process in processes:
        process.join()