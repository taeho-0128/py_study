#Kemija
#coci08c3p2

sentence = input()

decodedSentence = ''
i = 0
limit = 100

while i < len(sentence) and limit > 0 :
    decodedSentence = decodedSentence + sentence[i]
    if sentence[i] in 'aeiou':
        i = i + 3
    else:
        i = i + 1
print(decodedSentence)