import asyncio
import os
import threading
import edge_tts
import pygame
import time

# Voice configuration
VOICE = "en-AU-WilliamNeural"
BUFFER_SIZE = 1024

# Function to remove a file with retry mechanism
def remove_file(file_path):
    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
            break
        except Exception as e:
            print(f" Error removing file: {e}")
            attempts += 1
            time.sleep(1)

# Async function to generate TTS
async def generate_tts(TEXT, output_file):
    try:

        cm_txt = edge_tts.Communicate(TEXT, VOICE)
        await cm_txt.save(output_file)

    except Exception as e:
        print(f" Error: {e}")

# Function to play audio using pygame
def play_audio(file_path):
    try:
        print(" Playing audio...")
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(0.5)

        pygame.mixer.quit()
        # print(" Playback finished")
    except Exception as e:
        print(f" Error: {e}")

# Function to handle TTS and playback using threads
def speak(TEXT, output_file="output.mp3"):
    # Step 1: Generate TTS (async inside thread)
    tts_thread = threading.Thread(target=lambda: asyncio.run(generate_tts(TEXT, output_file)))
    tts_thread.start()
    tts_thread.join()

    # Step 2: Play audio if file exists
    if os.path.exists(output_file):
        play_thread = threading.Thread(target=play_audio, args=(output_file,))
        play_thread.start()
        play_thread.join()

    # Step 3: Remove audio file
    remove_file(output_file)



