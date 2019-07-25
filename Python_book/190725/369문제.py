# 369문제
# 정수 입력으로 이 게임이 끝나는 회차 번호가 주어진다.
# 1부터 그 회차까지 숫자가 프린트 되는데 3이 출력될 시 박수를 친다.
# 만약 3이 두번 나올시 (33, 36..) 박수가 두번!!
# 끝날때까지 박수 개수!!

n = int(input())

clap = 0
for i in range(0, n + 1):
        Str = str(i)
        for k in Str:
            if k == '3' or k == '6' or k == '9':
                clap += 1

print(clap)

