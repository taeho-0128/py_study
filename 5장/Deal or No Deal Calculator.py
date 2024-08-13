#Deal or No Deal Calculator
#ccc07j3

dollarcase = [100,500,1000,5000,10000,25000, 50000, 100000, 500000, 1000000]


opencnt = input()
if not opencnt.isdigit():
    exit('케이스 오픈 수가 숫자가 아님')
opencnt = int(opencnt)
if not 1<= opencnt <= 10:
    exit('오픈 카운트가 1~10이 아님')

for i in range(opencnt):
    open_num = input()
    if not open_num.isdigit():
        exit('오픈된 케이스 번호가 숫자가 아님')
    open_num = int(open_num)
    if not 1 <= open_num <= 10:
        exit('오픈된 케이스 번호가 1~10이 아님')
    dollarcase[open_num - 1] = 0



banker_offer = input()
if not banker_offer.isdigit():
    exit('뱅커의 제안금이 숫자가 아님')
banker_offer = int(banker_offer)
if not 10 < banker_offer:
    exit('뱅커의 제안금이 10달러 이하임')

notopen_cnt = 10 - opencnt
average_dollar = sum(dollarcase)/ notopen_cnt

if banker_offer > average_dollar:
    print('deal')
else:
    print('no deal')