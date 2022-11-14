"""
    Module that has all definitions for the bottom panel
"""
import tkinter as tk
from tkinter import messagebox, filedialog
import random
import datetime
from .calculator import calculator

# Same product numbers for every type in order to improve visuals
PRODUCTS = {
    "Food": [
        ("Chicken", 4.99),
        ("Soup", 2.49),
        ("Fish and chips", 3.29),
        ("Hamburger", 4.09),
        ("Kebab", 1.99)
    ],
    "Drink": [
        ("Water", 0.99),
        ("Coca-Cola", 2.45),
        ("Fanta", 2.45),
        ("Wine", 10.99),
        ("Beer", 4.99)
    ],
    "Dessert": [
        ("Ice cream", 1.50),
        ("Brownie", 1.80),
        ("Apple", 1.00),
        ("Orange", 1.00),
        ("Cheesecake", 3.59)
    ]
}
TAX: float = 0.21
PRODUCTS_ENTRY_TEXT: list = []
PRODUCTS_CHECKBUTTON: list = []
COST_ENTRIES: list = ["Food", "Drink", "Dessert", "Subtotal", "TAX", "Total"]
COST_ENTRY_TEXT: list = []
AREA_TEXT: tk.Text
PRODUCTS_PRICES: list = [0, 0, 0]
SUB_TOTAL: float = 0
TOTAL_PRICE: float = 0
INVOICE_NUMBER: float = 0


def bottom_panel(parent: tk.Frame):
    """ Creates two panels (right and left) in order to contain every element inside them
    :param parent: frame where all elements are attached
    """
    left = tk.Frame(
        parent, border=1, relief=tk.SOLID, background="azure3"
    )
    right = tk.Frame(
        parent, border=1, relief=tk.SOLID, background="azure3"
    )
    left.grid(row=0, column=0)
    right.grid(row=0, column=1)
    bp_left(left)
    bp_right(right)


# Left panel
def bp_left(parent: tk.Frame):
    """ Calls menu() and cost() in order to create elements
    :param parent: frame where all elements are attached
    :return:
    """
    menu(parent)
    cost(parent)


def menu(parent: tk.Frame):
    """ Creates a frame and a label_frame for the products
    :param parent: frame where all label_frames and checkbutton are attached
    """
    frame = tk.Frame(parent, border=1, relief=tk.FLAT)
    frame.grid(row=0, column=0)
    for index, title in enumerate(PRODUCTS.keys()):
        label_frame = tk.LabelFrame(
            frame, text=title, font=("Dosis", 14, "bold"),
            border=1, relief=tk.SOLID, foreground="black"
        )
        label_frame.grid(row=0, column=index)
        menu_checkbutton(label_frame, PRODUCTS[title])


def cost(parent: tk.Frame):
    """ Creates a frame and calls cost_entry in order to create entries inside
    :param parent: frame where cost entries are attached
    """
    frame = tk.Frame(
        parent, border=1, relief=tk.SOLID, padx=30
    )
    frame.grid(row=1, column=0)
    cost_entry(frame)


def menu_checkbutton(parent: tk.LabelFrame, products: [str]):
    """ Creates a checkbutton for every food, drink and dessert
    :param parent: frame where the checkbuttons are attached
    :param products: a list of strings
    """
    for index, product in enumerate(products):
        product_int_var = tk.IntVar()
        product_string_var = tk.StringVar()
        PRODUCTS_ENTRY_TEXT.append(product_string_var)
        product_string_var.set("0")
        product_entry = tk.Entry(
            parent, font=("Dosis", 12, "bold"), border=1, width=6,
            state=tk.DISABLED, textvariable=product_string_var
        )
        product_entry.grid(row=index, column=1)

        checkbutton = tk.Checkbutton(
            parent, text=product[0], font=("Dosis", 12, "bold"),
            onvalue=1, offvalue=0, variable=product_int_var,
            command=lambda
            int_var=product_int_var,
            entry=product_entry,
            entry_text=product_string_var:
            check_checkbutton(int_var, entry, entry_text)
        )
        PRODUCTS_CHECKBUTTON.append((product_entry, checkbutton, product_string_var))
        checkbutton.grid(row=index, column=0, sticky=tk.W)


def cost_entry(parent: tk.Frame):
    """ Creates entries for a list received as parameter
    :param parent: frame where the entries are attached
    """
    for index, entry in enumerate(COST_ENTRIES):
        cost_var = tk.StringVar()
        COST_ENTRY_TEXT.append(cost_var)
        cost_label = tk.Label(
            parent, text=entry, font=("Dosis", 12, "bold"),
            background="black", foreground="white"
        )
        entry = tk.Entry(
            parent, font=("Dosis", 12, "bold"), border=1, width=10,
            state="readonly", textvariable=cost_var
        )
        if index < 3:
            cost_label.grid(row=index, column=0)
            entry.grid(row=index, column=1, pady=5)
        else:
            cost_label.grid(row=index, column=2)
            entry.grid(row=index, column=3, pady=5)


def check_checkbutton(int_var: tk.IntVar, entry: tk.Entry, entry_text: tk.StringVar):
    """ Activates and deactivates an Entry and sets its text value
    :param int_var: tk.IntVar
    :param entry: Entry to be modified
    :param entry_text: text of the Entry
    """
    if int_var.get() == 1:
        entry.config(state=tk.NORMAL)
        entry.delete(0, tk.END)
        entry.insert(tk.END, "1")
        entry.focus()
    else:
        entry.config(state=tk.DISABLED)
        entry_text.set("0")


# Right panel
def bp_right(parent: tk.Frame):
    """ Creates the right bottom panel
    :param parent: frame where all panels are attached
    """
    calc_panel = tk.Frame(parent, relief=tk.FLAT)
    calc_panel.grid(row=0, column=0)
    text_area_panel = tk.Frame(parent, relief=tk.FLAT)
    text_area_panel.grid(row=1, column=0)
    buttons_panel = tk.Frame(parent, relief=tk.FLAT)
    buttons_panel.grid(row=2, column=0)
    calculator(calc_panel)
    text_area(text_area_panel)
    buttons(buttons_panel)


def text_area(parent: tk.Frame):
    """ Creates the text area that has the invoice information
    :param parent: frame where the text area is attached
    """
    global AREA_TEXT
    AREA_TEXT = tk.Text(parent, font=("Dosis", 12, "bold"),
                        border=1, width=42, height=10)
    AREA_TEXT.grid(row=4, column=0)


def buttons(parent: tk.Frame):
    """ Creates the buttons to control a text area
    :param parent: frame where the buttons are attached
    """
    button_names = ["total", "invoice", "save", "reset"]
    for index, name in enumerate(button_names):
        button = tk.Button(
            parent, text=name.title(), font=("Dosis", 12, "bold"),
            foreground="white", background="black",
            border=1, width=9)
        match name:
            case "total":
                button.config(command=total_button)
            case "invoice":
                button.config(command=invoice_button)
            case "save":
                button.config(command=save_button)
            case "reset":
                button.config(command=reset_button)
        button.grid(row=3, column=index)


def total_button():
    """ Prints the prices in the entry texts """
    set_prices()
    product_selected = \
        PRODUCTS_PRICES[0] != 0 or \
        PRODUCTS_PRICES[1] != 0 or \
        PRODUCTS_PRICES[2] != 0
    if product_selected:
        set_total_costs()
        AREA_TEXT.delete(1.0, tk.END)


def invoice_button():
    """ Prints an invoice in the text area """
    global INVOICE_NUMBER
    set_prices()
    product_selected = \
        PRODUCTS_PRICES[0] != 0 or \
        PRODUCTS_PRICES[1] != 0 or \
        PRODUCTS_PRICES[2] != 0
    if product_selected and len(AREA_TEXT.get(1.0, tk.END)) == 1:
        set_total_costs()
        AREA_TEXT.delete(1.0, tk.END)
        INVOICE_NUMBER = random.randint(1000, 9999)
        date = datetime.datetime.today().strftime("%H:%M - %d/%m/%Y")
        invoice_text = f"{date}\n" \
                       f"Invoice #{INVOICE_NUMBER}\n" \
                       f"Food: {'.'*60} {PRODUCTS_PRICES[0]} €\n" \
                       f"Drinks: {'.'*57} {PRODUCTS_PRICES[1]} €\n" \
                       f"Desserts: {'.'*53} {PRODUCTS_PRICES[2]} €\n" \
                       f"\nSubtotal:\t\t {SUB_TOTAL} €\n" \
                       f"TAX ({int(TAX * 100)}%):\t\t {round(SUB_TOTAL * TAX, 2)} €\n" \
                       f"Total:\t\t {TOTAL_PRICE} €"
        AREA_TEXT.insert(tk.END, invoice_text)


def save_button():
    """ Opens a file explorer to select a folder for saving the invoice """
    invoice_text = AREA_TEXT.get(1.0, tk.END)
    product_selected = \
        PRODUCTS_PRICES[0] != 0 or \
        PRODUCTS_PRICES[1] != 0 or \
        PRODUCTS_PRICES[2] != 0
    if product_selected and len(invoice_text) > 1:
        invoice_button()
        file = filedialog.asksaveasfile(
            mode="w",
            defaultextension=".txt",
            title="Save your invoice",
            initialfile=f"invoice_{INVOICE_NUMBER}"
        )
        if file:
            file.write(invoice_text)
            file.close()
            messagebox.showinfo("Saved!", "Your invoice has been saved")
        else:
            messagebox.showerror("Error!", "Your invoice has not been saved")
    else:
        messagebox.showerror("Error!", "Print your invoice by clicking on 'Invoice', then save it.")


def reset_button():
    """ Resets all to default values """
    AREA_TEXT.delete(1.0, tk.END)
    for i in range(6):
        COST_ENTRY_TEXT[i].set("")
    for entry, checkbutton, string_var in PRODUCTS_CHECKBUTTON:
        entry.config(state=tk.DISABLED)
        string_var.set("0")
        checkbutton.deselect()


def set_prices():
    """ Sets the product prices for each food, drink and dessert separately """
    global PRODUCTS_PRICES
    PRODUCTS_PRICES = [0, 0, 0]
    for index, entry in enumerate(PRODUCTS_ENTRY_TEXT):
        selected = int(entry.get())
        if selected > 0:
            if 0 <= index < 5:
                PRODUCTS_PRICES[0] += round(selected * PRODUCTS["Food"][index][1], 2)
            elif 5 <= index < 10:
                PRODUCTS_PRICES[1] += round(selected * PRODUCTS["Drink"][index - 5][1], 2)
            else:
                PRODUCTS_PRICES[2] += round(selected * PRODUCTS["Dessert"][index - 10][1], 2)


def set_total_costs():
    """ Sets the costs for the global variables, also sets them into entry texts """
    global SUB_TOTAL
    global TOTAL_PRICE
    SUB_TOTAL = round(sum(PRODUCTS_PRICES), 2)
    added_tax = round(SUB_TOTAL * TAX, 2)
    TOTAL_PRICE = round(SUB_TOTAL + added_tax, 2)

    for i in range(3):
        COST_ENTRY_TEXT[i].set(f"{PRODUCTS_PRICES[i]}")
    COST_ENTRY_TEXT[3].set(f"{SUB_TOTAL} €")
    COST_ENTRY_TEXT[4].set(f"{added_tax} €")
    COST_ENTRY_TEXT[5].set(f"{TOTAL_PRICE} €")
