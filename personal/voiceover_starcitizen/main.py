import keyboard as kb
import speech_recognition as sr
import pyttsx3
from tkinter import *
from time import sleep


WINDOW_TITLE: str = "StarCitizen - Voiceover"
WINDOW_RESOLUTION: str = "400x150+760+465"

active: bool = False
button: Button
info_text: Text
app = Tk()
audio = None
recognizer = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    recognizer.adjust_for_ambient_noise(source)
recognizer.pause_threshold = 0.8


def main():
    init_tkinter()

    # Informative text, service active (green) or stopped (red)
    global info_text
    info_text = Text(
        app, font=("Dosis", 12, "bold"), foreground="red", height=1
    )
    info_text.insert(END, "Servicio pausado")
    info_text.config(state=DISABLED)
    info_text.pack(side=TOP)

    # Button for activating or stopping the listening service
    global button
    button = Button(
        app, text="Start", width=15, height=2,
        command=lambda: button_listen()
    )
    button.pack(side=BOTTOM)

    app.mainloop()


def init_tkinter():
    app.title(WINDOW_TITLE)
    app.geometry(WINDOW_RESOLUTION)
    app.resizable(False, False)
    app.config(background="white")


def listening_callback(recognize, audio_data):
    try:
        listened = recognize.recognize_google(audio_data, language="es-ES")
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        speak("No se ha podido conectar con el servicio de reconocimiento de voz de Google."
              "Intentalo más tarde")
    else:
        commands(listened)


def button_listen():
    global active
    active = not active
    info_text.config(state=NORMAL)
    info_text.delete(1.0, END)
    if active:
        global audio
        button.config(text="Parar")
        info_text.config(foreground="green")
        info_text.insert(END, "Servicio activo")
        audio = recognizer.listen_in_background(source, listening_callback)
    else:
        button.config(text="Escuchar")
        info_text.config(foreground="red")
        info_text.insert(END, "Servicio pausado")
        stop_listening()
    info_text.config(state=DISABLED)


def commands(listened: str):
    if "tren de aterrizaje" in listened:
        kb.press_and_release("n")
        speak("El tren de aterrizaje está en movimiento.")
    elif "modo crucero" in listened:
        kb.press_and_release("c")
    elif "motor de salto" in listened:
        kb.press_and_release("b")
        speak("Iniciando sistemas, por favor espere.")
    elif "salto cuántico" in listened:
        kb.press("b")
        sleep(1)
        kb.release("b")
        speak("Viajando al destino fijado.")
    elif "energía" in listened:
        kb.press_and_release("u")
    elif "motores" in listened:
        kb.press_and_release("i")
    elif "para de escuchar" in listened:
        button_listen()
        speak("Vale, para volver a activarme dale al botón.")


def speak(message: str) -> None:
    """ Initiates the speech engine and says a message

    :param message: sentence to say
    """
    engine = pyttsx3.init()
    # TODO: do this for all pc
    # voice_id = 0 or 1 = english
    # voice_id = 2 = spanish
    voice_id = engine.getProperty("voices")[2].id
    engine.setProperty("voice", voice_id)
    engine.say(message)
    engine.runAndWait()


def start_listening():
    global audio
    audio = recognizer.listen_in_background(source, listening_callback)


def stop_listening():
    audio(wait_for_stop=False)


if __name__ == '__main__':
    main()
