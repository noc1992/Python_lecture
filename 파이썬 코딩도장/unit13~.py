a = list(map(int, input().split()))
b = list(map(int, input().split()))

Alice = 0
Bob = 0
for i in range(len(a)):
    if a[i] > b[i]:
        Alice = Alice + 1
    elif a[i] < b[i]:
        Bob = Bob + 1

fac = 1
for i in range(1, 11):
    fac *= i
import random as rd
dice1 = 0
dice2 = 0
count = 0
while True:
    dice1 = rd.randint(1, 6)
    dice2 = rd.randint(1, 6)
    hop = dice1 + dice2
    count += 1
    print(hop,count)
    if hop >= 10:
        break


for i in range(5):        # 0부터 4까지 5번 반복. 세로 방향
    for j in range(5):    # 0부터 4까지 5번 반복. 가로 방향
        if j == i:                # 세로 방향 변수와 같을 때
            print('*', end='')    # 별 출력. end에 ''를 지정하여 줄바꿈을 하지 않음
        else:                     # 세로 방향 변수와 다를 때
            print(' ', end='')    # 공백 출력. end에 ''를 지정하여 줄바꿈을 하지 않음
    print()

for i in reversed(range(5)):
    for k in range(i):
        print(' ', end='')
    print('*')

# bubble sort
aList = [3, 45, 21, 33, 56, 1, 11]

for i in range(len(aList)-1):
    for k in range(i+1, len(aList)):
        if aList[i] > aList[k]:
            aList[i], aList[k] = aList[k], aList[i]

print(aList)

for i in range(1, 101):
    if i % 15 == 0:
        i = "FizzBuzz"
        print(i)
    elif i % 3 == 0:
        i = 'Fizz'
        print(i)
    elif i % 5 == 0:
        i = "Buzz"
        print(i)
    else:
        print(i)


