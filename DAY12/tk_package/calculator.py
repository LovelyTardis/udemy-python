"""
    Module for calculator functions.
"""
import tkinter as tk

CALCULATOR_VISOR: tk.Entry
CALCULATOR_TEXT: str = ""


def calculator(parent: tk.Frame):
    """ Creates the layout for a calculator and implements functionality to the buttons
    :param parent: frame where the calculator is attached
    """
    global CALCULATOR_VISOR
    CALCULATOR_VISOR = create_calc_visor(parent)
    CALCULATOR_VISOR.grid(row=0, column=0, columnspan=4)
    calc_buttons = [["7", "8", "9", "+"],
                    ["4", "5", "6", "-"],
                    ["1", "2", "3", "*"],
                    ["=", "Back", "0", "/"]]
    for row in range(0, 4):
        for col in range(0, 4):
            button_value = calc_buttons[row][col].title()
            button = tk.Button(
                parent, text=button_value,
                font=("Dosis", 10, "bold"), foreground="white",
                background="azure4", border=1, width=8)
            button.config(command=lambda value=button_value: click_calculator(value))
            button.grid(row=row+1, column=col)


def create_calc_visor(parent: tk.Frame):
    """ Creates a tk.Entry for the received parent
    :param parent: frame where the visor is attached
    :return: created Entry
    """
    return tk.Entry(
        parent, font=("Dosis", 16, "bold"), width=32, border=1
    )


def click_calculator(btn_clicked: str):
    """ Depending on which button is clicked, calls back, reset or insert
    :param btn_clicked: string containing the calculator value
    """
    CALCULATOR_VISOR.delete(0, tk.END)
    if btn_clicked == "Back":
        back()
    elif btn_clicked == "=":
        result()
    else:
        insert(btn_clicked)


def insert(value: str):
    """ Inserts a value in the Entry text
    :param value: string added in the Entry text
    """
    global CALCULATOR_TEXT
    CALCULATOR_TEXT += value
    CALCULATOR_VISOR.insert(tk.END, CALCULATOR_TEXT)


def back():
    """ Deletes the last character in the Entry text """
    global CALCULATOR_TEXT
    if len(CALCULATOR_TEXT) != 0:
        text = list(CALCULATOR_TEXT)
        text.pop(-1)
        CALCULATOR_TEXT = "".join(text)
        CALCULATOR_VISOR.insert(tk.END, CALCULATOR_TEXT)


def result():
    """ Evaluates the calculator text and returns the value """
    global CALCULATOR_TEXT
    res: str = ""
    try:
        res = str(eval(CALCULATOR_TEXT))
    except ZeroDivisionError:
        res = "Can't divide by 0. Press '=' to reset"
    finally:
        CALCULATOR_TEXT = res
        CALCULATOR_VISOR.insert(tk.END, res)
