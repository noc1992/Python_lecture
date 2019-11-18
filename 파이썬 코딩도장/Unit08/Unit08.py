# 먼저 input 함수를 이용해 변수를 입력해 주는데 정수를 받기 때문에 map으로 인트를 안에 넣어주어야 함
# 그리고 불 함수를 이용해 합격 탈락을 표시해주는 것을 나타내고, 그 안에는 and를 넣어 하나라도 기준에 맞지
# 않으면 탈락(False)을 나타내게 함
# 심사문제 8
korean, english, mathematics, science = map(int, input().split(','))
print(bool(korean >= 90 and english > 80 and mathematics >85  and science >= 80))