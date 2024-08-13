#Card Game
#ccc99s1

NUM_CARD = 52

def no_high(lst):
    """
    lst는 카드를 나타내는 문자열의 리스트 입니다.
    lst에 높은 카드가 없으면 True를 반환하고 있으면 False를 반환합니다.
    """

    high_cards = {'jack', 'queen', 'king', 'ace'}
    for card in lst:
        if card in high_cards:
            return False
    return True

deck = []
for i in range(NUM_CARD):
    cardvalue = input()
    deck.append(cardvalue)

score_A = 0
score_B = 0
player = "A"

for i in range(NUM_CARD):
    card = deck[i]
    point = 0
    remainingcard_cnt = NUM_CARD - i - 1
    if card == 'jack' and remainingcard_cnt >= 1 and no_high(deck[i+1:i+2]):
        point = 1
    elif card == 'queen' and remainingcard_cnt >= 2 and no_high(deck[i+1:i+3]):
        point = 2
    elif card == 'king' and remainingcard_cnt >= 3 and no_high(deck[i+1:i+4]):
        point = 3
    elif card == 'ace' and remainingcard_cnt >= 4 and no_high(deck[i+1:i+5]):
        point = 4

    if point > 0:
        print(f'player {player} scores {point} point(s).')

    if player == "A":
        score_A += point
        player = "B"
    else:
        score_B += point
        player = "A"

print(f'player A: {score_A} point(s).')
print(f'player B: {score_B} point(s).')