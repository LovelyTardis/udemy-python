import keyboard as kb
from listening import speak, start_listening, stop_listening
from tkinter import *
from time import sleep
import json_commands as jc


WINDOW_TITLE: str = "Star Citizen - Voiceover"
WINDOW_RESOLUTION: str = "400x150+760+465"
COMMAND_LIST: list = []
FONTS: dict = {
    "service-label": ("Dosis", 12, "bold"),
    "info-frame": ("Dosis", 12, "bold"),
    "info-title": ("Dosis", 20),
    "title-command": ("Dosis", 18, "underline"),
    "info-command": ("Dosis", 18),
}

active: bool = False
button: Button
info_text: Label
app = Tk()
config_window: Toplevel


def main():
    init_config()
    init_tkinter()
    init_config_window()

    service_frame = Frame(app, border=0)
    service_frame.pack(side=TOP)
    # Informative text, service active (green) or stopped (red)
    Label(
        service_frame, font=FONTS["service-label"],
        height=1, background="white",
        text="Servicio:"
    ).grid(row=0, column=0)
    global info_text
    info_text = Label(
        service_frame, font=FONTS["service-label"], foreground="red",
        height=1, background="white"
    )
    info_text.config(text="pausado")
    info_text.grid(row=0, column=1)

    # Button for activating or stopping the listening service
    global button
    button = Button(
        app, text="Start", width=15, height=2,
        command=lambda: button_listen()
    )
    button.pack(side=BOTTOM)

    # Information button for showing a list of possible voice commands
    Button(
        app, text="Información", width=15, height=1,
        command=lambda: show_info_window()
    ).pack()

    app.mainloop()


def init_tkinter():
    app.title(WINDOW_TITLE)
    app.geometry(WINDOW_RESOLUTION)
    app.resizable(False, False)
    app.config(background="white")


def init_config():
    loaded_data = jc.load_json()
    for command in loaded_data:
        COMMAND_LIST.append(command)
    print("Init config complete!")
    print(COMMAND_LIST)


def init_config_window():
    global config_window
    config_window = Toplevel(app)
    config_window.title("Configuración de comandos")
    config_window.geometry("1280x720")
    Label(config_window, text="Configuración", font=FONTS["info-title"]).pack(side=TOP)

    frame = Frame(config_window)
    frame.pack(side=LEFT, expand=True, fill=BOTH)
    for i in range(5):
        option = ""
        match i:
            case 0:
                option = "Comando"
            case 1:
                option = "Información"
            case 2:
                option = "Tecla"
            case 3:
                option = "Modificador"
            case 4:
                option = "Modo"
        Label(
            frame,
            text=option,
            font=FONTS["info-command"],
        ).grid(
            row=0,
            column=i,
            sticky="w"
        )
    for i, command_row in enumerate(COMMAND_LIST):
        for j, data in enumerate(command_row):
            Label(
                frame,
                text=command_row[data],
                font=FONTS["title-command"] if j == 0 else FONTS["info-command"],
                wraplength=800
            ).grid(
                row=i + 1,
                column=j,
                sticky="w" if j < 2 else "n"
            )
    config_window.withdraw()


def show_info_window():
    global config_window
    try:
        if config_window.state() == "withdrawn":
            config_window.deiconify()
        elif config_window.state() == "normal":
            config_window.withdraw()
    except:
        init_config_window()
        config_window.deiconify()


def button_listen():
    global active
    active = not active
    if active:
        button.config(text="Parar")
        info_text.config(foreground="green", text="activo")
        app.iconify()
        speak("Voz activada")
        start_listening()
    else:
        button.config(text="Escuchar")
        info_text.config(foreground="red", text="pausado")
        stop_listening()


def commands(listened: str):
    for command in COMMAND_LIST:
        if command["name"] in listened:
            input_to_press = command["input"]
            match command["modifier"]:
                case 1:  # "control" modifier
                    input_to_press = "ctrl+" + input_to_press
                case 2:  # "alt" modifier
                    input_to_press = "alt+" + input_to_press
            match command["mode"]:
                case 0:  # press
                    kb.press_and_release(input_to_press)
                case 1:  # hold
                    kb.press(input_to_press)
                    sleep(1)
                    kb.release(input_to_press)


if __name__ == '__main__':
    main()
