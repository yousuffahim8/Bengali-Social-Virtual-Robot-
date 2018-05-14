from textblob import TextBlob
from PIL import Image

import time

input_statement = "Today I went to Barbeque Nation and the Food was awesome"
sentiment = TextBlob(input_statement)
print("Sentiment1 Score: ", sentiment.sentiment.polarity)  # Result = 1.0

if sentiment.sentiment.polarity >= -1 and sentiment.sentiment.polarity <= 0:
    image = Image.open('sad.png')
    image.show()
    image.close()
elif sentiment.sentiment.polarity >0  and sentiment.sentiment.polarity <= .3:
    image = Image.open('normal.png')
    image.show()
    image.close()
else:
    image = Image.open('smile.png')
    image.show()
    image.close()