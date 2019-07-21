#### 2차원 리스트 사용하기

### 2차원 리스트 만들고 요소에 접근하기
# * 리스트 = [[값, 값], [값,값], [값, 값]]
a = [[10, 20],
     [30, 40],
     [50, 60]]
a

## 2차원 리스트의 요소에 접근하기
# * 리스트[세로인덱스][가로인덱스]
# * 리스트[세로인덱스][가로인덱스]= 값
a[1][1] =1000 # 값할당

# 참고
# 톱니형 리스트
# # 2차원 리스트 [[10, 20], [30, 40], [50, 60]]은 가로 크기가 일정한 사각형 리스트입니다.
# # 특히 파이썬에서는 가로 크기가 불규칙한 톱니형 리스트(jagged list)도 만들 수 있습니다.
# #
# # a = [[10, 20],
# #      [500, 600, 700],
# #      [9],
# #      [30, 40],
# #      [8],
# #      [800, 900, 1000]]
# # 리스트 a는 가로 크기(행의 요소 개수) 가 제각각입니다.
# # 이런 리스트는 요소가 배치된 모양이 톱니처럼 생겼다고 하여 톱니형 리스트라고 부릅니다.
# #
# # 톱니형 리스트는 다음과 같이 append 메서드 등을 사용하여 동적으로 생성할 수도 있습니다.
# #
# # >>> a = []
# # >>> a.append([])
# # >>> a[0].append(10)
# # >>> a[0].append(20)
# # >>> a.append([])
# # >>> a[1].append(500)
# # >>> a[1].append(600)
# # >>> a[1].append(700)
# # >>> a
# # [[10, 20], [500, 600, 700]]

### 반복문으로 2차원 리스트의 요소를 모두 출력하기

## for 반복문을 한번만 사용하기
for x, y in a:
    print(x,y

## for 반복문을 두번 사용하기
for i in a:           # 전체 리스트에서 가로 한 줄씩 꺼내 옵니다.
    for j in i:                  #가로 한 줄(안쪽리스트) i 에서 요소를 하나씩 꺼냄
        print(j, end=' ')
    print()

## for와 range 사용하기
for i in range(len(a)):             # 세로크기
    for j in range(len(a[i])):      # 가로크기
        print(a[i][j], end=' ')
    print()

## while 반복문을 한번 사용하기
i = 0
while i < len(a):       # 반복할 때 리스트의 크기 활용(세로크기)
    x, y = a[i]         # 요소 두개를 한꺼번에 가져오기
    print(x, y)
    i += 1              # 인덱스를 1 증가시킴

## while 반복문을 두번 사용하기
i = 0
while i < len(a):
    j=0
    while j < len(a[i]):
        print(a[i][j], end=' ')
        j += 1
    print()          # 반복을 같은 줄에 넣으면 반복이 잘 되지 않음
    i += 1

### 반복문으로 리스트 만들기

## for 반복문으로 1차원 리스트 만들기
a = []
for i in range(10):
    a.append(0)
print(a)

## for 반복문으로 2차원 리스트 만들기
a = []

for i in range(3):
    line = []
    for j in range(2):
        line.append(j)
    a.append(line)

## 리스트 표현식으로 2차원 리스트 만들기
a = [[0 for j in range(2)] for i in range(3)]
# 반복문을 한번만 사용하고 싶다면 * 사용
a = [[0] * 2 for i in range(3)]  # [0] * 2 = [0,0]


## 톱니형 리스트 만들기
a = [1, 4, 2, 5, 7]
b = []

for i in a:
    line = []
    for j in range(i):
        line.append(0)
    b.append(line)

print(b)

a = [[0] * i for i in [4, 2, 1, 5, 7]]
a

# 참고
# sorted 로 2차원 리스트 정렬하기
# 2차원 리스트를 정렬할 때는 sorted() 함수를 사용합니다.

players = [
    ['stephen', 'A', 27],
    ['james', 'B', 28],
    ['kd', 'A+', 30]
]
print(sorted(players, key=lambda players: players[0]))  # 안쪽 리스트의 인덱스를 0번인덱스 기준으로 정렬하기
print(sorted(players, key=lambda players: players[1]))  # 안쪽 리스트의 인덱스를 2번인덱스 기준으로 정렬하기
