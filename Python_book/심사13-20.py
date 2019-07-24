# 심사문제 13
a = int(input())
b = input()

if b == "Cash3000":
    print(a - 3000)
elif b == "Cash5000":
    print(a - 5000)

# 심사문제 14
korean, english, math,sience = list(map(int, input().split()))

if 0 < korean <= 100 and 0 < english <= 100 and 0 < math <= 100 and 0 < sience <= 100:
    if bool(((korean+english+math+sience) / 4) > 80):
        print("합격")
    else:
        print("불합격")
else:
    print("잘못된 점수")

# 심사문제 15
age = int(input())
balance = 9000

if 7 <= age <= 12:
    balance -= 650
elif 13 <= age <= 18:
    balance -= 1050
else:
    balance -= 1250

print(balance)


# 심사문제 16
a = int(input())

for i in range(1,10):
    print(a ,'*', i, '=', a * i)

# 심사문제 17
a = int(input())
10000
while a >= 1350:
    print(a - 1350)
    a -= 1350

# 심사문제 18
start, stop = map(int, input().split())

i = start

while True:
    if i % 10 == 3:
        i += 1
        continue
    if i > stop:
        break
    print(i, end=' ')
    i += 1


# 심사문제 19
a = int(input())
5
for i in range(a):
    for j in range(a+i):
        if (a-1)-i <= j <= (a-1)+i:
            print('*', end='')
        else:
            print(' ', end='')
    print()

# 심사문제 20
a, b = list(map(int, input().split()))

i = a

for i in range(a, b+1):
    if i % 35 == 0:
        i = "FizzBuzz"
        print(i)
    elif i % 5 == 0:
        i = 'Fizz'
        print(i)
    elif i % 7 == 0:
        i = "Buzz"
        print(i)
    else:
        print(i)


