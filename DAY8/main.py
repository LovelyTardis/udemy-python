"""
    This day's project is a software for a numbered ticket dispenser.
    The project is divided in modules, located in package directory.
    IMPORTANT!
    I have two warnings from Pylint that I disabled:
        - "pylint: disable=possibly-unused-variable":
            Variables "ticket_1", "ticket_2", "ticket_3" are always used in line 32,
            but pylint doesn't know that.
        - "pylint: disable=broad-except":
            Errors are handled in main_functions module.
            I print the exception that comes from user_input function.
    Pylint passed by 10/10, but it's 7.89/10 without disabled warnings.
"""
from getpass import getpass
from os import system

from package import main_functions as mf


def main():
    """ Main function that runs all the execution. """
    # pylint: disable=possibly-unused-variable
    ticket_1, ticket_2, ticket_3 = mf.init_ticket()
    while True:
        mf.show_menu()
        try:
            area_input = mf.user_input()
        # pylint: disable=broad-except
        except Exception as err:
            print(err)
        else:
            num_ticket = (next(locals()[f"ticket_{area_input}"]), area_input)
            mf.show_ticket(num_ticket)
        pause_execution()


def pause_execution():
    """ Pauses the execution until ENTER is pressed and clears the console. """
    getpass("Press ENTER to continue")
    system("cls")


if __name__ == '__main__':
    main()
