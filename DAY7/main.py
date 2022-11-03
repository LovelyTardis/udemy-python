'''
    This day's project is about a simple bank account, where the user can deposit money and withdraw it.
    The program asks the user its name and surname, then creates a random value for the account number and sets the
    balance to 0€. The user can deposit money and withdrawn it.
    This project is for learning how Object-Oriented Programming (OOP) works in Python.
'''


import random
from getpass import getpass
from os import system

CUSTOM_PRINTS = {
    "client-created": "Client is successfully created!\n",
    "client-info": "Hello, {arg} {arg1}!\nYour currently balance is: {arg2}",
    "client-balance": "Your balance is {arg}€",
    "input-name": "Type your name: ",
    "input-surname": "Type your surname: ",
    "input-option": "Select an option above: ",
    "input-deposit": "How much money do you want to deposit? ",
    "input-withdraw": "How much money do you want to withdraw? ",
    "menu-1": "1. Make a deposit",
    "menu-2": "2. Withdraw money",
    "menu-3": "3. Sign out",
    "error-option-input": "The option has to be between 1 and 3\n",
    "error-withdraw": "Sorry, {arg} exceeds your currently balance.\n",
    "pause": "\n---- Press ENTER to continue ----\n",
    "goodbye": "\nThank you for using this app!\nHope we'll see you soon.",
}


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Client(Person):
    def __init__(self, name, surname, bank_number, balance=0):
        super().__init__(name, surname)
        self.bank_number = bank_number
        self.balance = balance

    def deposit(self, money):
        self.balance += money

    def withdraw(self, money):
        if money > self.balance:
            print(CUSTOM_PRINTS["error-withdraw"].format(arg=money))
        else:
            self.balance -= money

    def current_money(self):
        print(CUSTOM_PRINTS["client-balance"].format(arg=self.balance))

    def __str__(self):
        print(CUSTOM_PRINTS["client-info"].format(arg=self.name, arg1=self.surname, arg2=self.balance))


MENU_OPTIONS = 3


def main():
    option = 0
    client = initialize_client()
    client.__str__()
    pause_execution()
    while option != MENU_OPTIONS:
        clear()
        show_menu()
        try:
            option = int(input(CUSTOM_PRINTS["input-option"]))
            if option == MENU_OPTIONS:
                break
            if option < 1 or option > MENU_OPTIONS:
                raise Exception
        except:
            custom_print("error-option-input")
            pause_execution()
            continue
        execute_selected(option, client)
        pause_execution()
    custom_print("goodbye")
    pause_execution()


def initialize_client():
    name = input(CUSTOM_PRINTS["input-name"])
    surname = input(CUSTOM_PRINTS["input-surname"])
    return create_client(name, surname)


def create_client(name, surname):
    bank_number = random.randint(1000000, 9999999)
    client = Client(name, surname, bank_number)
    custom_print("client-created")
    return client


def show_menu():
    [custom_print(f"menu-{i}") for i in range(1, MENU_OPTIONS + 1)]


def execute_selected(option: int, client: Client):
    clear()
    match option:
        case 1:
            # deposit
            try:
                money = int(input(CUSTOM_PRINTS["input-deposit"]))
            except:
                custom_print("error-withdraw")
                pause_execution()
                return
            client.deposit(money)
        case 2:
            # withdraw
            try:
                money = int(input(CUSTOM_PRINTS["input-withdraw"]))
            except:
                custom_print("error-withdraw")
                pause_execution()
                return
            client.withdraw(money)
    client.current_money()


def pause_execution():
    getpass(CUSTOM_PRINTS["pause"])


def custom_print(custom_str: str):
    print(CUSTOM_PRINTS[custom_str])


def clear():
    system("cls")


main()
