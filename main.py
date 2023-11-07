import io
import os
import openai

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())


from openai import OpenAI
from pydub import AudioSegment
from pydub.playback import play
from tkinter import *

openai.api_key  = os.getenv('OPENAI_API_KEY')
print(openai.api_key)

client = OpenAI()

def stream_and_play(text):
  global button
  response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    #input=inputtxt.get(1.0, "end-1c") ,
    input=text,
  )

  # Convert the binary response content to a byte stream
  byte_stream = io.BytesIO(response.content)

  # Read the audio data from the byte stream
  audio = AudioSegment.from_file(byte_stream, format="mp3")

  # Play the audio
  play(audio)


if __name__ == "__main__":
  '''main = tkinter.Tk()
  inputtxt = Text(main,
                   height = 5,
                   width = 20)
  inputtxt.pack()
  button = Button(main, text = "Submit", command = stream_and_play)
  button.pack()
  main.mainloop()'''
  text = input("Enter text: ")
  stream_and_play(text)
