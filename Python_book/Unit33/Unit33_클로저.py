#### 클로저 사용하기

### 변수의 사용 범위 알아보기
x = 10                    # 전역변수
def foo():
    print(x)

foo()
print(x)


## 함수 안에서 전역 번수 변경하기
x = 10
def foo():
    x =20             # x 는 foo 안에서의 지역변수
    print(x)          # foo 지역변수 출력

foo()
print(x)


x = 10
def foo():
    global x =20             # 전역변수  x를 사용하겠다고 설정
    print(x)                 # 전역변수 출력

foo()
print(x)


### 함수 안에서 함수 만들기

# def 함수이름1():
   # 코드
     # def 함수이름2():
       # 코드

def print_hi():
