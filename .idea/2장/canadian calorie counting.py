#메뉴별 칼로리
burger1 = 461 #Cheeseburger
burger2 = 431 # Fish Burger
burger3 = 420 #Veggie Burger
burger4 = 0 #no burger

drink1 = 130 #Soft Drink
drink2 = 160 #Orange Juice
drink3 = 118 #Milk
drink4 = 0 #no drink

side1 = 100 #Fries
side2 = 57 #Baked Potato
side3 = 70 #Chef Salad
side4 = 0 #no side

dessert1 = 167 #Apple Pie
dessert2 = 266 #Sundae
dessert3 = 75 #Fruit Cup
dessert4 = 0 #no dessert

#버거 선택
burger = int(input())
if burger == 1:
    burger_calories = burger1
elif burger == 2:
    burger_calories = burger2
elif burger == 3:
    burger_calories = burger3
else:
    burger_calories = burger4

#음료 선택
drink = int(input())
if drink == 1:
    drink_calories = drink1
elif drink == 2:
    drink_calories = drink2
elif drink == 3:
    drink_calories = drink3
else:
    drink_calories = drink4


#사이드 선택
side = int(input())
if side == 1:
    side_calories = side1
elif side == 2:
    side_calories = side2
elif side == 3:
    side_calories = side3
else:
    side_calories = side4


#디저트 선택
dessert = int(input())
if dessert == 1:
    dessert_calories = dessert1
elif dessert == 2:
    dessert_calories = dessert2
elif dessert == 3:
    dessert_calories = dessert3
else:
    dessert_calories = dessert4

#전체 칼로리 계산
total_calorie = burger_calories + drink_calories  + side_calories + dessert_calories

print('Your total Calorie count is ' + str(total_calorie) + '.')