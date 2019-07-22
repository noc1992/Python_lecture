#### 함수 사용하기

### hi, world! 출력하기
# def 함수이름():
   # 코드

## 함수 만들기
def hi():
    print('hi, world!')

## 함수 호출하기
hi()


## 소스 파일에서 함수를 만들고 호출
def hi():
    print('ho, hihi')

hi()

## 함수의 실행 순서
# 1. 파이썬 스크립트 최초 실행
# 2. hi 함수 호출
# 3. hi 함수 실행
# 4. print 함수 실행 및 'hi, world!' 출력
# 5. hi 함수 종료
# 6. 파이썬 스크립트 종료


## 함수 작성과 함수 호출 순서
# 함수를 정의하기도 전에 호출하려고 하면 안된다.
# hi()
#
# def hi()   안됨


#  참고 빈 함수 만들기
def hi():
    pass


### 덧셈함수 만들기

# def 함수이름(변수1, 변수2)
   # 코드

def add(a, b):
    print(a + b)

# 참고 함수 독스트링 사용하기
def add(a, b):
    '''
    subtract
    :param a: integer
    :param b: integer
    :return: integer
    '''
    print(a + b)

?add

def add(a, b):
    return a + b

x = add(10, 30)

# 참고 return으로 함수 중간에서 빠져나오기
def not_ten(a):
    if a == 10:
        return
    print('10이 아님')

not_ten()

#return이 없는 함수 -> 리턴 타입이 보이드이다.

def grade_stu(a):
    if a >= 90:
        return 'A'
    if a >= 80:
        return 'B'
    if a >= 70:
        return 'C'
    if a >= 60:
        return 'D'
    return '...'

grade_stu(10)


### 함수에서 값을 여러개 변환하기
# def 함수이름(매개변수)
   # return 반환값1, 반환값2

def add_sub(a, b):
    return a + b, a - b

a, b = add_sub(1, 4)  # 언패킹으로 a와 b 안에 각각 넣어짐. 언패킹은 리스트와 튜플 모두 가능



###함수의 호출 과정 알아보기

def mySum(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum
a=30
mySum(a)
