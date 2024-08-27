#commonword
#cco99p2
from itertools import filterfalse
from pickletools import uint1

def checkNumber(num, min_val, max_val):
    if not min_val <= num <= max_val:
        exit(f"{num} is out of bounds ({min_val}-{max_val})")
    return num

def invert_dictionary(d):
    """
    d는 문자열을 숫자로 매핑하는 딕셔너리 입니다.
    d의 반전된 딕셔너리를 반환합니다.

    """
    inverted = {}
    for key in d:
        num = d[key]
        if not num in inverted:
            inverted[num] = [key]
        else:
            inverted[num].append(key)

    return inverted

def with_suffix(num):
    """
    num은 1보다 큰 정수
    5th와 같이 num에 접미사가 추가된 문자열을 반환합니다
    """
    s = str(num)
    if s[-1] == '1' and s[-2:] != '11':
        return s + 'st'
    elif s[-1] =='2' and s[-2:] != '12':
        return s + 'nd'
    elif s[-1] =='3' and s[-2:] != '13':
        return s + 'rd'
    else:
        return s + 'th'

def most_common_word(num_to_words,k):
    """
    num to word는 출현 빈도를 단어 리스트로 매핑한 딕셔너리 입니다.
    :param num_to_words:
    :param k:
    :return:
    """


    nums = list(num_to_words.keys())
    nums.sort(reverse=True)

    total = 0
    i = 0
    done = False
    while i < len(nums) and not done:
        num = nums[i]
        if total + len(num_to_words[num]) >=k:
            done = True
        else:
            total = total + len(num_to_words[nums])
            i += 1

    if total == k -1 and i <len(nums):
        return num_to_words[nums[i]]
    else:
        return []

n = int(input())

for dataset in range(n):
    lst = input().split()
    m = (lst[0])
    m = checkNumber(m,0,100)
    k =  lst[1]
    k = checkNumber(k,1,10000000)

    word_to_num = {}

    for i in range(m):
        word = input()
        if not word in word_to_num:
            word_to_num[word] = 1
        else:
            word_to_num[word] += 1
    num_to_words = invert_dictionary(word_to_num)

    orginal = with_suffix(k)
    words = most_common_word(num_to_words,k)

    print(f'{orginal} most common word(s):')
    for word in words:
        print(word)

    print()

