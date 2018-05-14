import pyaudio
import wave
import speech_recognition as sr
import pygame
from gtts import gTTS
from chatterbot import ChatBot
from textblob import TextBlob
from PIL import Image
from googletrans import Translator
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "voice.wav"

translator = Translator()
bot = ChatBot(
  'Ron Obvious',
   trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
logic_adapters=[
"chatterbot.logic.BestMatch"
    ]
)


#bot.train("chatterbot.corpus.english")
n = 0
r = sr.Recognizer()
while True:
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    print("* recording")
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    with sr.AudioFile("voice.wav") as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        n = n + 1
        #request = input('You: ')
        try:
            print(r.recognize_google(audio, language="bn"))
            request = r.recognize_google(audio,language="bn")
            translation = translator.translate(request, dest='en')
            translated_statement = str(translation.text)

            #print(translated_statement)

            sentiment = TextBlob(translated_statement)
            print("Sentiment1 Score: ", sentiment.sentiment.polarity)
            if sentiment.sentiment.polarity >= -1 and sentiment.sentiment.polarity < 0:
                image =Image.open('sad.png')
                image.show()
                image.close()
            elif sentiment.sentiment.polarity >= 0 and sentiment.sentiment.polarity <= .3:
                image =Image.open('normal.png')
                image.show()
                image.close()
            else:
                image =Image.open('smile.png')
                image.show()
                image.close()
            response = bot.get_response(translated_statement)
            translation = translator.translate(str(response), dest='bn')
            response = str(translation.text)
            print('Bot: ', response)
            tts = gTTS(text=str(response), lang='bn', slow='false')
            tts.save(str(n) + '.mp3')
            pygame.mixer.init()
            pygame.mixer.music.load(str(n) + '.mp3')
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                continue
        except:
            print("error")





