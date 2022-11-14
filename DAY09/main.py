"""
    This day's project is about a serial number search in written files.
    The program takes a MAIN_PATH and searches recursively in all directories for txt files.
    It calculates the took time to do the search and how much times it finds a serial number.
    When it finishes, shows in console a table with all that information.
"""
from pathlib import Path
from package.files import search_serial_numbers, show_result_files

MAIN_PATH = Path(Path().absolute(), "Main_Dir")


def main():
    """ Main function that calls package/files.py functions. """
    files, counter, time_took = search_serial_numbers(MAIN_PATH)
    show_result_files(files, counter, time_took)


if __name__ == '__main__':
    main()
