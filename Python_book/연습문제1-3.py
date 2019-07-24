# 연습문제 1
year = int(input())

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(year, "년은 윤년입니다.")
else:
    print(year, "년은 윤년이 아닙니다. ")

# 연습문제 2
H, M = list(map(int, input().split()))
18 45
if  0 <= H < 24:
    if (M - 45) < 0:
        M = 60 + (M - 45)
        H -= 1
        print("변경된 시간은", H,"시", M,"분 입니다.")
    elif (M - 45) >= 0:
        M -= 45
        H = H
        print("변경된 시간은", H, "시", M, "분 입니다.")

# 연습문제 3
a, b, c = list(map(int, input().split()))
d = [a,b,c]
for i in range(len(d)-1):
    for k in range(i+1, len(d)):
        if d[i] > d[k]:
            d[i], d[k] = d[k], d[i]

print(d.__getitem__(len(d)-2))


# 연습문제 4

for a in range(1,500):
  for b in range(a,500):
    for c in range(b,500):
      if a*a+b*b==c*c:
        if a+b+c==1000:
          print('a' ,'=', a, 'b','=', b, 'c','=',c)


# 연습문제 5
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 입력: 첫째 줄에 테스트 케이스의 개수 T를 입력받는다.
#       각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다.(0 < A, B < 10)
# 출력: 각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다.
#       x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B이다.

x = int(input())

for i in range(x):
    A, B = list(map(int, input().split()))
    C = (A + B)
    print("Case #",(i+1),": ", A, "+", B, "=", C)


# 연습문제 6
n = int(input())
height = (n + 1) // 2

for i in range(1, height + 1):
    for k in range(height - i):
        print(' ', end='')
    for k in range(i * 2 - 1):
        print('*', end='')
    print()
for i in reversed(range(1, height)):
    for k in range(i, height):
        print(' ', end='')
    for k in range(i * 2 - 1):
        print('*', end='')
    print()



# 반복문 3
# 디지털 시계에 하루동안(00:00~23:59) 3이 표시되는 시간을 초로 환산하면
# 총 몇 초(second) 일까요?- 디지털 시계는 하루동안 다음과 같이 시:분(00:00~23:59)으로 표시됨.
# 00:00 (60초간 표시)		00:01 		…		23:59
total = 0
for hour in range(24):
    if hour % 10 == 3:          # 3시, 13시, 23시
        total += 60 * 60;
    else:
        for min in range(60):
            if min // 10 == 3:  # 30분 ~ 39분
                total += 60
            elif min % 10 == 3: # 3분, 13분, 23분, 43분, 53분
                total += 60

print(total)



def is_palindrome(n):
  s = str(n)
  return s == s[::-1]