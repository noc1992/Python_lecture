# 표준 입력으로 문자열 여러 개와 숫자 여러 개가 두 줄로 입력되고,
# 첫 번째 줄은 키, 두 번째 줄은 값으로 하여 딕셔너리를 생성합니다.
# 다음 코드를 완성하여 딕셔너리에서 키가 'delta'인 키-값 쌍과 값이 30인
# 키-값 쌍을 삭제하도록 만드세요.

# 입력
# alpha bravo charlie delta echo foxtrot golf
# 30 40 50 60 70 80 90
# 결과
# {'bravo': 40, 'charlie': 50, 'echo': 70, 'foxtrot': 80, 'golf': 90}

keys = input().split()
values = map(int, input().split())

x = dict(zip(keys, values))

x = {key : value for key, value in x.items() if (value != 30 and key != "delta")}

print(x)