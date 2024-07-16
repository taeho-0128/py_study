#AmeriCanadian
#ccc02j2


#모음 (y도 모음)
vowels = "aeiouy"


while True:
    word = input()
    if len(word) > 64:
        exit("단어 64자 초과")

    if word == 'quit!':
        break
    #4자 이상이고, 어미로 자음뒤에 or이 오는 경우 our로 변경
    if len(word) > 4 and word[-2:] == 'or' and word[-3] not in vowels:
        word = word[:-2] + 'our'
        print(word)
    else:
        print(word)