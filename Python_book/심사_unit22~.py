# 심사문제 22
# 표준 입력으로 정수 두 개가 입력됩니다(첫 번째 입력 값의 범위는 1~20, 두 번째 입력 값의 범위는 10~30이며 첫 번째 입력 값은 두 번째 입력 값보다 항상 작습니다).
# 첫 번째 정수부터 두 번째 정수까지를 지수로 하는 2의 거듭제곱 리스트를 출력하는 프로그램을 만드세요
# (input에서 안내 문자열은 출력하지 않아야 합니다). 단, 리스트의 두 번째 요소와 뒤에서 두 번째 요소는 삭제한 뒤 출력하세요. 출력 결과는 리스트 형태라야 합니다.

start, stop = list(map(int, input().split()))
1 10
i = 0
my = [2 ** i for i in range(start, stop+1)]
my.pop(1)
my.pop(-2)
print(my)

# 심사문제 23
col, row = list(map(int, input().split()))

matrix = []
for i in range(row):
    matrix.append(list(input()))




