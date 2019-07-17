# 연습문제 1
year = int(input())

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(year, "년은 윤년입니다.")
else:
    print(year, "년은 윤년이 아닙니다. ")

# 연습문제 2
def FortyFive(a, b):
    if (b - 45) < 0:
        a -= 1 and b == (60 - (b - 45))
        if b == 60:
            a += 1
    elif (b - 45) == 0:
        return (a = a and b = 0)
    else:
         return (a=a and b = (b - 45))
     print("적용된 시간은 ", a,"시 ", b, "분 입니다.")


H, M = list(map(int, input().split()))
12 32
FortyFive(H, M)