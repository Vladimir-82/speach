from gtts import gTTS
from playsound import playsound


text_val = 'No description, website, or topics provided.'
language = 'en'


obj = gTTS(text=text_val, lang=language, slow=False)
obj.save("minus.mp3")


playsound("minus.mp3")