#bard
#crci06p1

def checkNumber(num, min_val, max_val):
    if not min_val <= num <= max_val:
        exit(f"{num} is out of bounds ({min_val}-{max_val})")
    return num


# 입력을 정수로 변환하고 범위 검사
total_villager = int(input())
total_villager = checkNumber(total_villager, 2, 100)

total_dinner = int(input())
total_dinner = checkNumber(total_dinner, 1, 50)


villager_songs = {i: set() for i in range(1, total_villager + 1)}


song_number = 1
for _ in range(total_dinner):
    dinner_participantlst = input().split()
    participant_cnt = int(dinner_participantlst[0])
    dinner_participant = [int(x) for x in dinner_participantlst[1:]]


    if 1 in dinner_participant:
        new_song = song_number
        song_number += 1
        for villager in dinner_participant:
            villager_songs[villager].add(new_song)
    else:
        shared_songs = set()
        for villager in dinner_participant:
            shared_songs.update(villager_songs[villager])
        for villager in dinner_participant:
            villager_songs[villager].update(shared_songs)

all_songs = set(range(1, song_number))
villagers_who_know_all_songs = [villager for villager, songs in villager_songs.items() if songs == all_songs]

for villager in sorted(villagers_who_know_all_songs):
    print(villager)
