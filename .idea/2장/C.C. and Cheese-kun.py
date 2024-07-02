#피자의 폭
pizza_width = int(input())
#피자의 치즈 비율
pizza_cheesins = int(input())

#피자의 폭은 1~3까지이다
if (1 > pizza_width or 3 < pizza_width):
    exit()

#치즈 비율은 0 ~ 100까지 이다
if (0 > pizza_cheesins or 100 < pizza_cheesins):
    exit()



#너비가 3이고 치즈 비율이 95% 이상이면 absolutely
if pizza_width == 3 and pizza_cheesins >= 95:
    pizza_satisfied = ('absolutely')
#너비가 1이고 치즈 비율이 50% 이하이면 fairly
elif pizza_width == 1 and pizza_cheesins <= 50:
    pizza_satisfied = ('fairly')

# 나머지는very
else:
    pizza_satisfied = ('very')


print(f'C.C. is {pizza_satisfied} satisfied with her pizza.')