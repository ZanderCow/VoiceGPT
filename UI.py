from Recorder import Recorder
import tkinter as tk
from Transcriber import Transcriber
from Chatbot import Chatbot

class UI:
    """
    this class handles everything for the UI

    Attributes:
        self.root : tk.Tk()
            - main tkinter window.
            - handles ui related stuff.
        self.recorder : Recorder()
            - recorder instance object from the Recorder class.
            - recorders the user 
        self.ai : Chatbot
            - chatgpt bot that talks to the user
        self.start_button : tk.Button()
            - tkinter button that when clicked will record the users voice
        self.stop_button : tk.Button()
            - tkinter button that stops the recording
            - only appears when the self.start_button has been clicked
         


    """
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")


        self.recorder = Recorder()
        self.ai = Chatbot("act as a chatbot")
    

        self.start_button = tk.Button(self.root, text='Record', command=self.start_record)
        self.start_button.pack()
        self.stop_button = tk.Button(self.root, text='Stop Recording', command=self.stop_record)
    

    def run(self):
        self.root.mainloop()



    def start_record(self):
        """
        This function starts the recording process. 
        It hides the start button, initiates the recording process, and then displays the stop button.
        """
        self.start_button.pack_forget()
        self.recorder.start_recording()
        self.stop_button.pack()
        

    def stop_record(self):
        """
        This function stops the recording process. 
        It hides the stop button, displays the start button, and stops the recording process. 
        It then transcribes the recorded audio to text, sends the transcribed text to the GPT-3 model for processing, and prints the model's response.
        """
        self.stop_button.pack_forget()
        self.start_button.pack()
        self.recorder.stop_recording()
        print()
        
        transribed_text = Transcriber.convert_speech_to_text('StoredAudioFiles/userinput.wav')

        response = self.ai.ask_gpt3(transribed_text)
        
        print(response)
        return 

    





