#Magnus
#coci18c3p1

#주어진 단어
word = input()

if not word.isupper:
    exit("영어가 대문자가 아님")
if not 1<=len(word)<= 100000:
    exit("word 길이가 100000초과함")


foundH = 0
foundHO = 0
foundHON = 0
foundHONI = 0

for i in word:
    if i == 'H':
        foundH += 1
    if i == 'O' and foundH >= 1:
        foundHO +=1
    if i == 'N' and foundHO >= 1:
        foundHON += 1
    if i== 'I' and foundHON >= 1:
        foundHONI += 1
        foundH = 0
        foundHO = 0
        foundHON = 0

print(foundHONI)