### 25-1 딕셔너리 응용하기

# 키 - 값 쌍 추가하기


# setdefault  쌍추가  * 값이 없으면 에러가 남
x = {'a' : 10, 'b': 20, 'c' : 30, 'd' : 40}
x.setdefault('e')
x

x.setdefault('f', 100)
x

# update 값 수정 키 없으면 추가 * 키가 문자일 경우에만 해당됨. 숫자의 경우 update(딕셔너리)와 같이 사용해야함
x.update(e = 50)
x

# 키 - 값 쌍 삭제 * pop(키)는 딕셔너리에서 특정 키 값 쌍을 삭제한뒤 '값' 을 반환
x.pop()         # 없는 값을 팦하면 기본값을 반환한다. 그러나 반환값이 없으면 에러

# del 특정값 삭제
del x['c']
x

# 임의의 키- 값 삭제하기  popitem()
x.popitem()

# clear 모든 값 삭제
x.clear()

# 키의 값 가져오기
x.get('a')

# 키 - 값 쌍을 모두 가져오기
# item() 쌍을 모두 가져옴 keys() 키를 모두 가져옴 values() 값을 모두 가져옴
x.items()
x.keys()
x.values()

# 리스트와 튜플로 딕셔너리 만들기
y = dict.fromkeys(keys)

# defaultdict 기본값이 0 인 딕셔너리 만들기
from collections import defaultdict
z = defaultdict(int)
p = defaultdict(lambda : 'alpha')   # 기본지정값을 정해주는 코드 lambda
p['a']


### 25-2 반복문으로 딕셔너리의 키 - 값 쌍을 모두 출력
for i in x:
    print(i, end=' ')
x
# 키 - 값 모두 출력
for key, value in x.items():   # x에 키-값 쌍을 꺼내서 키-key 값-value에 저장하고 꺼낼때마다 코드 반복
    print(key, value)          # 따라서 print로 key와 value를 출력하면 키-값 쌍을 모두 출력 가능

# 키 만 출력
for key in x.keys():
    print(key, end=' ')

# 값 만 출력
for value in x.values():
    print(value, end=' ')


### 25-3 딕셔너리 표현식 사용하기
# 반복문 사용

keys
x = {key: value for key,value in dict.fromkeys(keys).items()}
x

#키만 가져와서 특정값을 넣거나 values로 값을 가져온되 키로 사용 가능
{key:30 for keys in dict.fromkeys(keys).keys()}
{key: 0 for key in dict.fromkeys(['a', 'b', 'c', 'd']).keys()}
{value: 0 for value in {'a': 10, 'b': 20, 'c': 30, 'd': 40}.values()}
{key: 0 for key in dict.fromkeys({'a': 10, 'b': 20, 'c': 30, 'd': 40}).keys()}
{key: 30 for key in dict.fromkeys(keys).keys()}


# 딕셔너리 표현식에서 if 조건문 사용하기 / 특정 키 - 값을 삭제하려면? -> del

# for key,value in x.items():
#     if value == 20 or key == "delta":
#         del x[key]                          이거 안됨 밑에 코드가 되는 코드


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

# 딕셔너리 중첩
terrestrial_planet = {
    'Mercury': {
        'mean_radius': 2439.7,
        'mass': 3.3022E+23,
        'orbital_period': 87.969
    },
    'Venus': {
        'mean_radius': 6051.8,
        'mass': 4.8676E+24,
        'orbital_period': 224.70069,
    },
    'Earth': {
        'mean_radius': 6371.0,
        'mass': 5.97219E+24,
        'orbital_period': 365.25641,
    },
    'Mars': {
        'mean_radius': 3389.5,
        'mass': 6.4185E+23,
        'orbital_period': 686.9600,
    }
}

print(terrestrial_planet['Venus']['mean_radius'])  # 6051.8
# 중첩 딕셔너리는 계층형 데이터를 저장할 때 유용합니다.
# 딕셔너리 안에 들어있는 딕셔너리에 접근하려면 딕셔너리 뒤에 [ ](대괄호)를 단계만큼 붙이고 키를 지정해주면 됩니다.
# 딕셔너리[키][키]
# 딕셔너리[키][키] = 값

# 여기서는 딕셔너리가 두 단계로 구성되어 있으므로 대괄호를 두 번 사용합니다.
# 그래서 금성(Venus)의 반지름(mean radius)를 출력하려면 다음과 같이 먼저
# 'Venus'를 찾아가고 다시 'mean_radius'의 값을 가져오면 됩니다.

print(terrestrial_planet['Venus']['mean_radius'])    # 6051.8