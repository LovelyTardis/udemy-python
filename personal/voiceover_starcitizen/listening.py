import speech_recognition as sr
import pyttsx3

audio = None
recognizer = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    recognizer.adjust_for_ambient_noise(source)
recognizer.pause_threshold = 0.8


def listening_callback(recognize, audio_data):
    try:
        listened = recognize.recognize_google(audio_data, language="es-ES")
    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        speak("No se ha podido conectar con el servicio de reconocimiento de voz de Google."
              "Intentalo más tarde")
    else:
        return listened


def start_listening():
    global audio
    audio = recognizer.listen_in_background(source, listening_callback)


def stop_listening():
    audio(wait_for_stop=False)


def speak(message: str) -> None:
    """ Initiates the speech engine and says a message

    :param message: sentence to say
    """
    es_voice_id = 0
    engine = pyttsx3.init()
    for i, voice in enumerate(engine.getProperty("voices")):
        # if not in all, it will get first voice ( 0 )
        if "Spanish" in voice.name:
            es_voice_id = i
            break
    voice_id = engine.getProperty("voices")[es_voice_id].id
    engine.setProperty("voice", voice_id)
    engine.say(message)
    engine.runAndWait()
