"""
    Module that has a function that searches for serial numbers in files.
    It also has a show function, that prints a table with the information.
"""
import math
import time
import datetime
import re
from pathlib import Path


TODAY = datetime.date.today().strftime("%d/%m/%Y")
SEARCH_PATTERN = r"N\w{3}-\d{5}"
CUSTOM_PRINTS = {
    "table-start": f"Search date: {TODAY}\n\nFILE\t\tSERIAL NUM\n{'-'*10}\t{'-'*10}",
    "table-end": "\nFound serial numbers: {arg0}\nSearch took {arg1} second/s",
}


def search_serial_numbers(path: Path):
    """ Receives a path for searching in it, checks if every file has the pattern
    :param path: the directory where it searches (also subdirectories)
    :return: list containing tuples, counter, took time
    """
    s_time = time.time()
    counter = 0
    files = []
    for file in path.glob("**/*.txt"):
        file_checked = re.search(SEARCH_PATTERN, file.open().read())
        if file_checked is not None:
            counter += 1
            files.append((file.name, file_checked.group()))
    e_time = time.time()
    time_took = math.ceil(e_time - s_time)
    return [files, counter, time_took]


def show_result_files(files: [tuple], counter: int, time_took: int):
    """ Prints a table that contains the today date, a list of files and its serial number,
        the total serial numbers found and how much time it took to do the search
    :param files: list of tuples (filename, serial_number)
    :param counter: number of times it found a serial number
    :param time_took: number of seconds that needed to complete the search
    """
    print(CUSTOM_PRINTS["table-start"])
    for file in files:
        print(f"{file[0]}\t{file[1]}")
    print(CUSTOM_PRINTS["table-end"].format(arg0=counter, arg1=time_took))
