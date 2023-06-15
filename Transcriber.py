import openai

class Transcriber:
    """
    transcribes a audiofile to text to allows for it to be inputted into the chatbot
    """
    def convert_speech_to_text(audio_file_location):
        with open(audio_file_location, "rb") as audio_file:
            transcript = openai.Audio.transcribe(
                file = audio_file,
                model = "whisper-1",
                response_format="text",
                language="en"
            )
        return transcript


    