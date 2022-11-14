"""
    Module for voice functions.
"""
import speech_recognition as sr
import pyttsx3


def listen() -> str:
    """ Opens the default microphone and to listen to it for a voice input

    :return: string text of what listened or an error as string
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as micro:
        recognizer.pause_threshold = 0.8
        audio = recognizer.listen(micro)
        try:
            listened_audio = recognizer.recognize_google(audio, language="en-EN")
            return listened_audio.lower()
        except sr.UnknownValueError:
            return "Error: unknown value error"
        except sr.RequestError:
            return "Error: request error"
        except:
            return "Error: unknown error"


def speak(message: str) -> None:
    """ Initiates the speech engine and says a message

    :param message: sentence to say
    """
    engine = pyttsx3.init()
    voice_id = engine.getProperty("voices")[1].id
    engine.setProperty("voice", voice_id)
    engine.say(message)
    engine.runAndWait()
