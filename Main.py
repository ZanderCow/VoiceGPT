import os
import openai
from Chatbot import Chatbot
from UI import UI
from Recorder import Recorder
from Transcriber import Transcriber

os.environ['OPENAI'] = 'put api key here'
openai.api_key = os.environ["OPENAI"]














ui = UI()
ui.run()


