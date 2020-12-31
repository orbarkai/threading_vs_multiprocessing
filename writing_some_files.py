"""
An example of writing files with:
 * Single threaded
 * Multithreaded
 * Multiprocessed
"""

import time
import threading
import multiprocessing
import os.path

FILES_DIRECTORY = 'written_files'
NUMBER_OF_FILES = 100
FILE_SIZE = 10 * 1024 * 1024
CHUNK_SIZE = 1024


def write_file(file_name):
    """
    Write a single file to the written files directory

    :param str file_name: The name of the file to write
    """

    with open(os.path.join(FILES_DIRECTORY, file_name), 'wb') as file_object:
        for i in range(FILE_SIZE / CHUNK_SIZE):
            file_object.write('A' * CHUNK_SIZE)


def single_threaded_write_files():
    """
    Write the files with a single thread
    """

    start_time = time.time()
    for thread_number in xrange(NUMBER_OF_FILES):
        write_file('file-{}.txt'.format(thread_number))
    end_time = time.time()
    print "Single threaded execution time: {exec_time}s".format(exec_time=end_time - start_time)


def threaded_write_files():
    """
    Write the files with a multithreading
    """

    start_time = time.time()
    thread_list = []
    for thread_number in xrange(NUMBER_OF_FILES):
        write_thread = threading.Thread(target=write_file,
                                        args=('file-{}.txt'.format(thread_number),))
        write_thread.start()
        thread_list.append(write_thread)
    for write_thread in thread_list:
        write_thread.join()
    end_time = time.time()
    print "Multi threaded execution time: {exec_time}s".format(exec_time=end_time - start_time)


def processed_write_files():
    """
    Write the files with a multiprocessing
    """

    start_time = time.time()
    process_list = []
    for thread_number in xrange(NUMBER_OF_FILES):
        write_thread = multiprocessing.Process(target=write_file,
                                               args=('file-{}.txt'.format(thread_number),))
        write_thread.start()
        process_list.append(write_thread)
    for write_thread in process_list:
        write_thread.join()
    end_time = time.time()
    print "Multi processed execution time: {exec_time}s".format(exec_time=end_time - start_time)


def main():
    """
    Runs all the execution types
    """

    threaded_write_files()
    single_threaded_write_files()
    processed_write_files()


if __name__ == '__main__':
    main()
