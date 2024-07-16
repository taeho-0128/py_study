#Cold Compress
#ccc19j3

messages_count = int(input())

while messages_count > 0:
    messages_count -= 1
    message = input()
    thisword = 0
    nextword= thisword + 1
    word_count = 1

    while thisword < len(message):
        if nextword < len(message) and message[thisword] == message[nextword]:
            word_count += 1
        else:
            print(word_count, message[thisword], end=' ')
            word_count = 1
        thisword += 1
    print()




