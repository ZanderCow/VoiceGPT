import tkinter as tk
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

class Recorder:
    """
    this class handles the recording related stuff

    Attributes: 
        self.recording : list
            - list where the recording is stored
        self.steam : sd.InputSteam()
            - a recording steam where recording information is temperarly kept as a buffer as chunks and then added
            to self.recording.

    """
    def __init__(self):
        self.recording = None
        self.stream = None

    def start_recording(self):
        self.recording = []
        self.stream = sd.InputStream(callback=self.audio_callback)
        self.stream.start()

    def audio_callback(self, indata, frames, time, status):
        self.recording.append(indata.copy())

    def stop_recording(self):
        self.stream.stop()
        self.stream.close()
        self.stream = None

        # Concatenate all recorded numpy arrays into one
        final_recording = np.concatenate(self.recording, axis=0)

        # Save the recording to an output file
        wav.write('StoredAudioFiles/userinput.wav', 44100, final_recording)

