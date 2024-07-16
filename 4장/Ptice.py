
#Ptice
#coci08c1p2

questioncnt = input()
correctAnswer = input()

questioncnt = int(questioncnt)
if not 1 <= questioncnt <= 100:
    exit('문제 수가 올바르지 않습니다')

adrianAnswer = ""
brunoAnswer = ""
goranAnswer = ""

# Adrian의 답
i = 0
while i < questioncnt:
    if i % 3 == 0:
        adrianAnswer += 'A'
    elif i % 3 == 1:
        adrianAnswer += 'B'
    else:
        adrianAnswer += 'C'
    i += 1

# Bruno의 답
i = 0
while i < questioncnt:
    if i % 4 == 0:
        brunoAnswer += 'B'
    elif i % 4 == 1:
        brunoAnswer += 'A'
    elif i % 4 == 2:
        brunoAnswer += 'B'
    else:
        brunoAnswer += 'C'
    i += 1

# Goran의 답
i = 0
while i < questioncnt:
    if i % 6 == 0:
        goranAnswer += 'C'
    elif i % 6 == 1:
        goranAnswer += 'C'
    elif i % 6 == 2:
        goranAnswer += 'A'
    elif i % 6 == 3:
        goranAnswer += 'A'
    elif i % 6 == 4:
        goranAnswer += 'B'
    else:
        goranAnswer += 'B'
    i += 1

correctAdrian = 0
correctBruno = 0
correctGoran = 0

# 정답 비교 및 점수 계산
j = 0
while j < questioncnt:
    if adrianAnswer[j] == correctAnswer[j]:
        correctAdrian += 1
    if brunoAnswer[j] == correctAnswer[j]:
        correctBruno += 1
    if goranAnswer[j] == correctAnswer[j]:
        correctGoran += 1
    j += 1


maxcorect = max(correctAdrian, correctBruno, correctGoran)

winners = []
if correctAdrian == max_correct:
    winners.append("Adrian")
if correctBruno == max_correct:
    winners.append("Bruno")
if correctGoran == max_correct:
    winners.append("Goran")

for winner in sorted(winners):
    print(winner)

