#문제 수
question_cnt = int(input())

#문제수 10,000개 초과
if not  0 <question_cnt <10000:
    exit('문제 수10,000개 초과')

# 학생이낸 답
student_answer =''
for i in range(question_cnt):
    student_answer += input()

# 올바른 답
correct_answer = ''
for i in range(question_cnt):
    correct_answer += input()

#학생의 답이 올바른답인 경우
correct = 0
for i in range(question_cnt):
    if correct_answer[i] == student_answer[i]:
        correct += 1

print(correct)

