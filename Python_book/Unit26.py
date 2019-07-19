### 세트 사용하기

# 세트 만들기
# 세트는 {} 안에 값을 저장하며 각 값은, (콤마)로 구분해 줍니다.
# * 세트 = {값1, 값2, 값3}

fruits = {'mellon', 'watermellon', 'strawberry','blueberry'} # 세트는 요소 중복 안됨
fruits

# 특히 세트는 []로 요소출력 안됨

# 세트에 특정 값이 있는지 확인하기
'orange' in fruits
'mellon' not in fruits

# set를 사용하여 세트 만들기
# * set(반복가능한 객체)

set('the_game_of_throne') # 유일한 문자만 세트로 만듦
# {'_', 'a', 'e', 'f', 'g', 'h', 'm', 'n', 'o', 'r', 't'}

# 그리고 set(range(3)) 와같이 숫자를 만들어 내는 range를 사용하면 0-4까지 숫자를 가진 세트를 만들수 있슴
b = set(range(4))
b

# 빈세트
c = set()
c
# c= {}는 세트로 만들어지지 않음

# 한글세트도 가능
set('왕좌의 게임')

# 세트 안에 세트 안들어감

# 프로즌 세트 -> 내용변경 안되는 세트
d = frozenset(range(5)) # 집합연산 메서드에서 요소추가 삭제 연산 메서드 사용불가

# frozenset는 세트를 세트안에 넣고 싶을때 사용함.