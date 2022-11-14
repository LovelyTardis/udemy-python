"""
    This day's project is about a voice recognition for console.
    It has responses depending on what the user says.
    The main inputs are:
        - bye: to end the assistant
        - open YouTube: to open YouTube main page
        - open GitHub: to open my GitHub page
        - joke: to tell a random joke
        - today: to say today's date
        - search in wikipedia...: to search in wikipedia whatever you want.
                                  For example: "search in wikipedia Albert Einstein"
    If it is not getting what the user says, it will say it doesn't have an answer.
"""
import webbrowser
import wikipedia
import pyjokes
from voice_recognition import voice, date_time


def main():
    """ Main application """
    voice.speak(initial_salute())
    check_voice()


def check_voice():
    """ The main loop that keeps listening until it recognizes any of the commands """
    while True:
        message = voice.listen()
        if "bye" in message:
            voice.speak("Thanks for using this assistant. Good bye!")
            break
        if "open youtube" in message:
            voice.speak("opening youtube")
            webbrowser.open("https://www.youtube.com")
        elif "open github" in message:
            voice.speak("opening LovelyTardis' github")
            webbrowser.open("https://github.com/LovelyTardis")
        elif "joke" in message:
            joke = pyjokes.get_joke("en", "all")
            voice.speak(f"Listen to this joke: {joke}")
        elif "today" in message:
            voice.speak(date_time.get_today())
        elif "search in wikipedia" in message:
            voice.speak("Searching in wikipedia")
            message = message.replace("search in wikipedia", "")
            wikipedia.set_lang("en")
            res = wikipedia.summary(message, sentences=1)
            voice.speak(f"Done! Wikipedia says: {res}")
        else:
            voice.speak("Sorry, I have no answer for that")


def initial_salute() -> str:
    """ Builds the first salute

    :return: string to say
    """
    return f"{date_time.daytime_salute()}! What can I do for you?"


if __name__ == '__main__':
    main()
