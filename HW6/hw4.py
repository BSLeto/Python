# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


text = 'Lorem Ipабвsum - это табвекст-"рабвыба", частабво используемый в печати и вабвэбабв-дизайне.\
    Lorem Ipsum является стандартнабвой "рыбоабвй" для текстоабвв на латинице с начала XVI века.'

def del_word(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

text = del_word(text)
print (text)