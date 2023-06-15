import openai

class Transcriber:
    """
    transcribes a audiofile to text to allows for it to be inputted into the chatbot
    """
    def convert_speech_to_text(audio_file_location):
        """
        converts text to speech using whisper API

        Params:
            audio_file_location : string
                - string version of a pathfile to the audio file location
        
        Returns: 
            transcript : string 
                - a transcribed text of the audio file 
        """
        with open(audio_file_location, "rb") as audio_file:
            transcript = openai.Audio.transcribe(
                file = audio_file,
                model = "whisper-1",
                response_format="text",
                language="en"
            )
        return transcript


    