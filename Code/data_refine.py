import re


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
    text = re.sub(r"n'", "ng", text)
    text = re.sub(r"'bout", "about", text)
    text = re.sub(r"'til", "until", text)
    text = re.sub(r"  ", "", text)
    text = re.sub(r"   ", "", text)
    text = re.sub(r"[-()\"#/@;:<>{}`+=~|.!?¿🎸🎤🎉,📈💥😂😁👻🤖🙈😱🙆😔😕😳😄☺😊😅️😏😒😀😐😴😝❤😍😭😄😘💀😋😉🤔🌙🔌🤓🙂😆😥🙁😃😘🤓😶💔😖😲😵😵😠🤕🤒😞👋😞🍿🌨😯💃👍]", "", text)

    return text


lines1=open('C:/Users/Fahim/Desktop/Final_thesis/Rdany_question.txt',encoding='utf8').read().split('\n')
path=''
train_bangla1 = open(path + 'Rdany_question.txt','a',encoding='utf8')
i=0
for line in lines1:
    lines1[i]=clean_text(lines1[i])
    train_bangla1.write(str(lines1[i]) + '\n')
    i+=1
