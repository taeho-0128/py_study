input_file = open('lostcow.in', 'r')
location_list = input_file.readline().split()
input_file.close()

firstfarmer_loca = int(location_list[0])
cow_loca = int(location_list[1])

def checkNumber(num, min_val, max_val):
    if not min_val <= num <= max_val:
        exit(f"{num} is out of bounds ({min_val}-{max_val})")
    return num

firstfarmer_loca = checkNumber(firstfarmer_loca, 0, 1000)
cow_loca = checkNumber(cow_loca, 0, 1000)

total_distance = 0
current_position = firstfarmer_loca
step = 1

while True:
    next_position = firstfarmer_loca + step

    if (firstfarmer_loca < cow_loca and next_position >= cow_loca) or (firstfarmer_loca > cow_loca and next_position <= cow_loca):
        total_distance += abs(cow_loca - current_position)
        break

    total_distance += abs(next_position - current_position)
    current_position = next_position
    step *= -2


output_file = open('lostcow.out', 'w')
output_file.write(f"{total_distance}\n")
output_file.close()