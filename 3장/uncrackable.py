#uncrakable
#wc17c3j3

password = input()


upper = 0
lower = 0
digit = 0

# 패스워드의 대문자, 소문자, 숫자의 수를 측정
for char in password:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
    elif char.isdigit():
        digit += 1

# 패스워드는 8~12자 이내여야 함
# 비밀번호 통과 규칙은 3개 이상의 소문자, 2개 이상의 대문자, 1개 이상의 0 ~ 9까지의 자연수가 들어가야 함
if 8 <= len(password) <= 12 and lower >= 3 and upper >= 2 and digit >= 1:
    print('Valid')
else:
    print('Invalid')