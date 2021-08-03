from gtts import gTTS
import os

#enter the text in quotes to convert into audio remember to be connected to internet ass gtts requires internet connection
text = """  your text here  """
language='en'
speech = gTTS(text=text, lang=language, slow=False)
speech.save("audio.mp3")
os.system("start audio.mp3")

