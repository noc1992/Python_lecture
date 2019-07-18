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
a = int(input())
7
for i in range(a):
    for j in range(a+i):
        if (a-3)-i <= j <= (a-3)+i:
            print('*', end='')
        else:
            print(' ', end='')
    print()

j < (i-2) or j >= (a+1)-i:
