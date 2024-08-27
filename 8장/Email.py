#Email
#ecoo19r2p1

def checkNumber(num, min_val, max_val):
    if not min_val <= num <= max_val:
        exit(f"{num} is out of bounds ({min_val}-{max_val})")
    return num


def clean(address):
    """
    address는 이메일 주소를 나타내는 문자열 입니다.

    정리된 이메일 주소를 반환합니다.
    """

    # +기호와 @ 기호 사이의 모든 문자를 제거
    plus_index = address.find('+')
    if plus_index != -1:
        at_index = address.find('@')
        address = address[:plus_index] + address[at_index:]

    # @ 기호 앞에 있는 모든 점을 제거
    at_index = address.find('@')
    before_at = ''
    i = 0
    while i < at_index:
        if address[i] != '.':
            before_at = before_at + address[i]
        i = i + 1
    cleaned = before_at + address[at_index:]

    # 소문자로 변환

    cleaned = cleaned.lower()

    return cleaned

for dataset in range(10):
    email_cnt = input()
    email_cnt = checkNumber(email_cnt,1,100000)
    addresses = set()
    for i in range(email_cnt):
        address = input()
        address = clean(address)
        addresses.add(address)

    print(len(addresses))
