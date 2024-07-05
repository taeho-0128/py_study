# 전체 문자 메시지
messages = input()
if not 1 < len(messages) <255:
    exit('문자 길이가 1~255자가 아님')


# 행복 이모티콘
happyface = ':-)'
# 슬픔 이모티콘
sadface = ':-('

# 행복한 얼굴 수
cnt_happyface = messages.count(happyface)
# 슬픈 얼굴 수
cnt_sadface = messages.count(sadface)

# 행복한 얼굴 수, 슬픈 얼굴 수 둘 다 0이면 none
if cnt_happy_emo == 0 and cnt_sad_emo == 0:
    print('none')
# 행복한 얼굴 수 > 슬픈 얼굴 수이면 happy
elif cnt_happy_emo > cnt_sad_emo:
    print('happy')
# 행복한 얼굴 수 < 슬픈 얼굴 수이면 sad
elif cnt_sad_emo > cnt_happy_emo:
    print('sad')
# 나머지(행복한 얼굴 = 슬픈 얼굴 수이면 unsure)
else:
    print('unsure')