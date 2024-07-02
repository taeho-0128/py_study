# 전체 메시지
messages = input()

# 행복 이모티콘
happy_emo = ':-)'
# 슬픔 이모티콘
sad_emo = ':-('

# 행복 이모티콘 수
cnt_happy_emo = messages.count(happy_emo)

# 슬픔 이모티콘 수
cnt_sad_emo = messages.count(sad_emo)

# 행복 이모티콘 수, 슬픔 이모티콘 수 둘 다 0이면 none
if cnt_happy_emo == 0 and cnt_sad_emo == 0:
    print('none')
# 행복 이모티콘 수 > 슬픔 이모티콘 수이면 happy
elif cnt_happy_emo > cnt_sad_emo:
    print('happy')
# 행복 이모티콘 수 < 슬픔 이모티콘 수이면 sad
elif cnt_sad_emo > cnt_happy_emo:
    print('sad')
# 나머지(행복 이모티콘 수 = 슬픔 이모티콘 수이면 unsure)
else:
    print('unsure')