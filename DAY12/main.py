"""
    DISCLAIMER: I know that the colors and visuals are poor, but remember I am not a designer,
                I just make the app runs as fluent as I can. *The important here is the code.*
    This day's project is about a desktop application for controlling a restaurant invoices.
    It is like a cash register:
        - on the left side has all food, drink and desserts with checkbutton to select what
          and how much the client ordered a product.
        - on the right side has a calculator, a text area and buttons to print the total money
          or the invoice, or save the invoice, or reset the text area.
"""
import tkinter as tk
from tk_package.title_frame import title_panel
from tk_package.bottom_frames import bottom_panel


# Assuming screen is 1920x1080 (16:9)
WINDOW_RESOLUTION = "1020x630+450+200"
WINDOW_TITLE = "LovelyTardis restaurant - Invoice Manager"
MAIN_COLOR = "azure3"


def main():
    """ Main definition, calls modules in the "tk_package" package """
    app = tk.Tk()
    init_window(app)
    title_panel(app, title="Invoice manager", background=MAIN_COLOR)
    bottom_frame = tk.Frame(
        app, border=1, relief=tk.FLAT
    )
    bottom_frame.pack(side=tk.TOP)
    bottom_panel(bottom_frame)
    app.mainloop()


def init_window(app: tk.Tk):
    """ Initializes the main tkinter application and sets it up """
    app.title(WINDOW_TITLE)
    app.geometry(WINDOW_RESOLUTION)
    app.resizable(False, False)
    app.config(background=MAIN_COLOR, pady=10, padx=10)


if __name__ == '__main__':
    main()
