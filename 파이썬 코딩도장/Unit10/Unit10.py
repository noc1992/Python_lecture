# 먼저 input으로 값을 받아야 하는데 인트값을 받기로 했으니 인트를 밖에 씌워준다.
# 다음으로 범위설정을 위해 range함수를 사용한다. 입력받은 숫자를 사용하기 위해 a를 맨 뒤
# range(시작:끝:사용할 값) 에 넣어준다. 그것을 튜플화 하기위해 튜플을 사용해 주면 됨

# 심사문제 10
a = int(input())
print(tuple(range(-10, 10, a)))