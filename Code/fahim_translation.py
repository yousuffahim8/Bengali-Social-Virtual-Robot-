import re, math
from googletrans import Translator
from collections import Counter
translator=Translator()
WORD = re.compile(r'\w+')
lines1=open('C:/Users/Fahim/Desktop/Final_thesis/QUE_Bangla.txt',encoding='utf8').read().split('\n')
lines2=open('C:/Users/Fahim/Desktop/Final_thesis/Questions_final2.txt',encoding='utf8').read().split('\n')
path=''
train_bangla1 = open(path + 'bangla_convn.txt','a',encoding='utf8')
file=[]
def clean_text(text):
    '''Clean text by removing unnecessary characters and altering the format of words.'''

    text = text.lower()
    text = re.sub(r"i'm", "i am", text)
    text = re.sub(r"he's", "he is", text)
    text = re.sub(r"she's", "she is", text)
    text = re.sub(r"it's", "it is", text)
    text = re.sub(r"that's", "that is", text)
    text = re.sub(r"what's", "that is", text)
    text = re.sub(r"where's", "where is", text)
    text = re.sub(r"how's", "how is", text)
    text = re.sub(r"\'ll", " will", text)
    text = re.sub(r"\'ve", " have", text)
    text = re.sub(r"\'re", " are", text)
    text = re.sub(r"\'d", " would", text)
    text = re.sub(r"\'re", " are", text)
    text = re.sub(r"won't", "will not", text)
    text = re.sub(r"can't", "cannot", text)
    text = re.sub(r"n't", " not", text)
    return text
def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator
def text_to_vector(text):
     text = text.lower()
     text=clean_text(text)
     words = WORD.findall(text)
     return Counter(words)
i=13340
num=0
for j in range(0, 39516):
    translation = translator.translate(lines1[i], dest='en')
    english1= str(translation.text)
    text1=lines2[i]
    text2=english1
    vector1 = text_to_vector(text1)
    vector2 = text_to_vector(text2)
    cosine1 = get_cosine(vector1, vector2)
    i=i+1
    translation = translator.translate(lines1[i], dest='en')
    english2 = str(translation.text)
    text1 = lines2[i]
    text2 = english2
    vector1 = text_to_vector(text1)
    vector2 = text_to_vector(text2)
    cosine2 = get_cosine(vector1, vector2)
    cosine= cosine1+cosine2
    #print(cosine)
    if cosine>1.6:
            train_bangla1.write(lines1[i-1] + '\n')
            train_bangla1.write(lines1[i] + '\n')
            num=num+1
            print("Total Taken",i)
    i=i+1
