import time
import os
import platform
import wave
import threading
import pyaudio


def play_audio(file_path):
    try:
        with wave.open(file_path, "rb") as wav_file:
            audio_data = wav_file.readframes(wav_file.getnframes())

        if platform.system() == "Windows":
            import winsound

            winsound.PlaySound(file_path, winsound.SND_FILENAME)
        else:
            filename = "sound.wav"

            # Set chunk size of 1024 samples per data frame
            chunk = 1024

            # Open the sound file
            wf = wave.open(filename, "rb")

            # Create an interface to PortAudio
            p = pyaudio.PyAudio()

            # Open a .Stream object to write the WAV file to
            # 'output = True' indicates that the sound will be played rather than recorded
            stream = p.open(
                format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True,
            )

            # Read data in chunks
            data = wf.readframes(chunk)

            # Play the sound by writing the audio data to the stream
            while data != "":
                stream.write(data)
                data = wf.readframes(chunk)

            # Close and terminate the stream
            stream.close()
            p.terminate()

    except Exception as e:
        print(f"Error while playing audio: {e}")


def main():
    audio_file_path = "sound.wav"
    play_audio(audio_file_path)
    while True:
        current_time = time.localtime()
        if current_time.tm_min == 0:
            threading.Thread(target=play_audio, args=(audio_file_path,)).start()
        time.sleep(60)  # Wait for a minute before checking again


if __name__ == "__main__":
    main()
