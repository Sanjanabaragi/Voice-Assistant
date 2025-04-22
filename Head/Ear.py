import speech_recognition as sr
from mtranslate import translate
from colorama import Fore, init
import threading
import time

init(autoreset=True)

listening = False  # Global flag to control animation


# 🎨 Animation thread: shows only while listening is active
def print_loop():
    while True:
        if listening:
            print(Fore.LIGHTGREEN_EX + "I am Listening...     ", end="\r", flush=True)
        time.sleep(0.1)


# 🌐 Translate Hindi to English
def Trans_hindi_to_english(txt):
    try:
        english_txt = translate(txt, to_language="en")
        return english_txt
    except Exception as e:
        return f"Translation error: {e}"


# 🎤 Listen, recognize, translate, and print the translated text
def listen():
    global listening
    recognizer = sr.Recognizer()

    # Adjusting listening sensitivity
    recognizer.dynamic_energy_threshold = False  # Disable dynamic energy threshold adjustment
    recognizer.energy_threshold = 35000  # Lower this value to make the recognizer more sensitive
    recognizer.pause_threshold = 0.3  # Increase this if you want the recognizer to wait for a pause
    recognizer.non_speaking_duration = 0.1  # Make sure non_speaking_duration is not greater than pause_threshold
    recognizer.dynamic_energy_ratio = 1.5  # Increase if more sensitivity is needed
    recognizer.dynamic_energy_adjustment_damping=0.004
    recognizer.operation_timeout=None


    threading.Thread(target=print_loop, daemon=True).start()  # Start animation once

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjusting for ambient noise

        while True:
            try:
                listening = True
                print(Fore.CYAN + "\nYou can speak now...")
                audio = recognizer.listen(source, timeout=8)  # Increased timeout
                listening = False

                recognized_txt = recognizer.recognize_google(audio, language="hi-IN").lower()
                translated_txt = Trans_hindi_to_english(recognized_txt)

                # Print the translated English text
                print(Fore.GREEN + f" {translated_txt}")

            except sr.UnknownValueError:
                listening = False
                print(Fore.LIGHTRED_EX + "Sorry, I didn't catch that.")
            except sr.RequestError as e:
                listening = False
                print(Fore.LIGHTRED_EX + f"Request Error: {e}")
            except Exception as e:
                listening = False
                print(Fore.LIGHTRED_EX + f"Error: {e}")



# 🟢 Entry point
while True:
    listen()
