"""
    Module that has all definitions for the title panel.
"""
import tkinter as tk


def title_panel(app: tk.Tk, title: str, background: str):
    """ Creates a frame that packs in TOP with a label
    :param app: main application
    :param title: text that will be in the label
    :param background: string color
    :return:
    """
    frame = tk.Frame(app, border=1, relief=tk.SOLID)
    frame.pack(side=tk.TOP)
    title_label = tk.Label(frame, text=title, width=26, foreground="black",
                           font=("Dosis", 48), background=background)
    title_label.grid(row=0, column=0)
