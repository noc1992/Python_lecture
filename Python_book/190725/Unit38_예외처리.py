def ten_div(x):
    return 10/x
ten_div(0)


## 예외의 에러 메세지 받아오기
y = [10, 20, 30]
try:
    index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
    print(y[index] / x)
except ZeroDivisionError as e:    # 예외가 발생했을 때 실행됨
    print('예외가 발생했습니다.', e)
except IndexError as e:
    print('잘못된 인덱스 입니다.', e)


### else와 finally 사용하기
try:
    x = int(input('숫자:'))
    y = 10 / x
except ZeroDivisionError:
    print('0은 못나눠')
else:
    print(y)
finally:
    print('코드 끝')
