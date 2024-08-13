#timus
#2144


#입력 읽기
def read_boxes(n):
    """
    n은 읽어야할 상자 수 입니다.
    """
    boxes = []
    for i in range(n):
        box = input().split()
        box.pop(0)
        for i in range(len(box)):
            box[i] = int(box[i])
            boxes.append(box)
    return boxes


#모든 박스들이 정상인지 확인한다

def all_boxes_ok(boxes):
    """
    boxes는 확인 해야 할 상자 리스트 입니다.
    피규어 높이가 점점 커지면 true를 반환하고 아니면 false를 반환합니다.
    """
    for i in range(len(boxes)-1):
        if (boxes[i] > boxes[i+1]):
            return False
    return True

#상자의 양 끝값 얻기
def boxes_endpoints(boxes):
    """
    boxes는 상자들의 리스트입니다.
    각 박스는 액션 피규어의 높이를 가진 리스트 입니다.

    각 상자 리스트의 양 끝 값을 반환합니다.
    양끝값은 가장 왼쪽에 있는 피규어의 높이와
    가장 오른쪽에 있는 피규어의 높이 입니다.
    """
    endpoints = []
    for box in boxes:
        endpoints.append(box[0],box[-1])
    return endpoints

#양 끝값이 정상인지 확인
def all_endpoints_ok(endpoints):
    """
    endpoints는 두 개의 값을 가진 리스트 입니다.
    두 개의 값은 상자의 가장 왼쪽과 오른쪽 피규어의 높이 입니다.

    endpoints가 순서대로 정리가 가능하면 true를 반환하고 그렇지 않으면 false를 반환합니다.
    """
    maximum = endpoints[0][1]



# 정렬이 가능한지 확인
def all_endpoints_ok(endpoints):
    """
    endpoints는 두개의 값을 가진 리스트 입니다.
    두 개의 값은 상자의 양 끝값을 말합니다.

    요구 사항: endpoints는 피규어의 높이 순서대로 정렬되어야 함

    endpoints가 순서대로 정리가 가능한 상자들이라면 True를 반환하고,
    그렇지 않으면 False를 반환합니다.
    """

    maximum = endpoints[0][1]
    for i in range(1,len(endpoints)):
        if endpoints[i][0] < maximum
            return False
        maximum = endpoints[i][1]
    return True

#main program
totalBox = input()
if not totalBox.isdigit():
    exit('상자수가 숫자가 아님')
totalBox = int(totalBox)
if not 1<= totalBox <= 100:
    exit('상자수가 1~100이 아님')
boxes = read_boxes(totalBox)

#모든 상자가 정상인지 확인
if not all_boxes_ok(boxes):
    print('No')
else:
    endpoints = boxes_endpoints(boxes)

    #새로운 상자들을 정렬
    endpoints.sort()

    #정렬된 상자들 정리할 수 있는지 결정
    if all_endpoints_ok(endpoints):
        print('YES')
    else:
        print('NO')
