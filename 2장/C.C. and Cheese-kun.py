#피자의 폭
pizza_width = int(input())
#피자의 치즈 비율
pizza_cheesins = int(input())

#피자의 폭은 1~3까지이다
if not  1 <pizza_width < 3:
    exit('피자의 폭이 1~3이 아님')

#치즈 비율은 0 ~ 100까지 이다
if not 0 < pizza_cheesins < 100:
    exit('치즈 비율이 0~100이 아님')


#너비가 3이고 치즈 비율이 95% 이상이면 피자 만족도는 absolutely
if pizza_width == 3 and pizza_cheesins >= 95:
    pizza_satisfied = ('absolutely')

#너비가 1이고 치즈 비율이 50% 이하이면 피자 만족도는 fairly
elif pizza_width == 1 and pizza_cheesins <= 50:
    pizza_satisfied = ('fairly')

# 나머지의 피자 만족도는 very
else:
    pizza_satisfied = ('very')


print(f'C.C. is {pizza_satisfied} satisfied with her pizza.')