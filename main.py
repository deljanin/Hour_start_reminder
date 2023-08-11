import time
import threading
import os
import platform
import sys
import pygame


def get_audio_file_path():
    return "sound.wav"  # Replace with the actual path to your audio file


def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()


def main():
    audio_file_path = get_audio_file_path()
    play_audio(get_audio_file_path())
    while True:
        current_time = time.localtime()
        if current_time.tm_min == 0:
            threading.Thread(target=play_audio, args=(audio_file_path,)).start()
        time.sleep(60)  # Wait for a minute before checking again


if __name__ == "__main__":
    main()
