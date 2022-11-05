"""
    This day's project is a software for a numbered ticket dispenser.
    The project is divided in modules, located in package directory.
    Pylint passed by 10/10.
"""
from getpass import getpass
from os import system

from package import main_functions as mf


def main():
    """ Main function that runs all the execution. """
    tickets = mf.init_tickets()
    while True:
        mf.show_menu()
        try:
            area_input = mf.user_input()
        except TypeError as err:
            print(err)
        except ValueError as err:
            print(err)
        else:
            num_ticket = (next(tickets[area_input]), area_input)
            mf.show_ticket(num_ticket)
        pause_execution()


def pause_execution():
    """ Pauses the execution until ENTER is pressed and clears the console. """
    getpass("Press ENTER to continue")
    system("cls")


if __name__ == '__main__':
    main()
