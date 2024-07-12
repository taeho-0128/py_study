WandWizard = input()

dueltimes = input()
dueltimes= int(dueltimes)

if not 1<= dueltimes <=100:
    exit("듀얼 횟수 너무 많음")

obeyWizardcnt = 1
obeyWizard = WandWizard + ''

for i in range(dueltimes):
    wizardDule = input()
    winner = wizardDule [0]
    loser = wizardDule [2]

    if loser == WandWizard:
        WandWizard = winner
        if  winner not in obeyWizard:
            obeyWizard += winner
            obeyWizardcnt += 1

print(WandWizard)
print(obeyWizardcnt)
