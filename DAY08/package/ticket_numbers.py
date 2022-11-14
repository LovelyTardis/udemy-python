"""
    Module that has a function to be imported in "main_functions" module.
    Pylint passed by 10/10.
"""


def ticket_generator():
    """ Generator that yields the next ticket. """
    counter = 1
    while True:
        yield counter
        counter += 1
