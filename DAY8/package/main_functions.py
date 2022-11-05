"""
    Module that has the main functions for the Day 8 project.
    It imports the ticket_numbers.py module.
    Pylint passed by 10/10.
"""
from .ticket_numbers import ticket_generator
MENU_OPTIONS = {
    1: "Baby care",
    2: "Cosmetic items",
    3: "Antibiotics",
}
TOTAL_AREAS = len(MENU_OPTIONS)
ERRORS = {
    "type": "\nYou must type a number.\n",
    "value": "\nYou typed a number that is not an option.\n",
}


def user_input():
    """ Show a prompt and waits the user to type a number.
    :returns: integer
    :exception TypeError: If not a number
    :exception ValueError: If forbidden number
    """
    try:
        selected = int(input("Which area do you want a ticket? "))
    except ValueError as _:
        raise TypeError(ERRORS["type"]) from _
    else:
        if selected < 1 or selected > TOTAL_AREAS:
            raise ValueError(ERRORS["value"])
        return selected


def show_ticket(ticket: tuple):
    """ Prints the ticket information simulating the ticket issuance.
    :param ticket: tuple
    """
    print(f"\nQueue number "
          f"{MENU_OPTIONS[ticket[1]][0]}-{ticket[0]}"
          f"\nfor {MENU_OPTIONS[ticket[1]]}\n")


def show_menu():
    """ Prints the MENU_OPTIONS for a TOTAL_AREAS range.
    :returns: list(print)
    """
    return [print(f"{i}. {MENU_OPTIONS[i]}") for i in range(1, TOTAL_AREAS + 1)]


def init_tickets():
    """ Calls ticket_generator() for a range in TOTAL_AREAS and assigns the value to a dictionary.
    :returns: dict(...Generator)
    """
    tickets = dict()
    for i in range(1, TOTAL_AREAS + 1):
        tickets[i] = ticket_generator()
    return tickets
