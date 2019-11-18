#### 함수에서 위치인수와 키워드 인수 사용하기

### 위치 인수와 리스트 언패킹 사용하기
print(10, 20, 30)


## 위치 인수를 사용하는 함수를 만들고 호출하기
def print_number(a, b, c):
    print(a)
    print(b)
    print(c)


## 언패킹 사용하기
# * 함수(*리스트)
# * 함수(*튜플)


## 가변인수 함수 만들기
# * def 함수이름(*매개변수):
   # 코드

def print_numbers(*args)
    for arg in args:
        print(arg)



# 참고
# 고정인수와 가변인수를 함께 사용하기
def print_numbers(a, *args):       # 가변인수가 고정인수 앞에 (*args, a) 이러면 *안됨!!!
    print(a)
    print(args)


### 키워드 인수 사용하기
def personal_info(name, age, address):
    print('이름' , name)
    print('나이' , age)
    print('주소' , address)

personal_info('stephen', 30, 'US, okland')         # 입력순서가 바뀌면 이름이 30이 될수 있음
personal_info(age=30, address='서울시 용산구 이촌동', name='홍길동')   # 이렇게 하면 순서 안바뀜

# 참고 sep, end 또한 키워드 인수


### 키워드 인수와 딕셔너리 언패킹 사용하기
# * 함수(**딕셔너리)
x = {'name':'stephen', 'age':30 , 'address' : 'US, okland'}
personal_info(**x)

personal_info(**{'name':'stephen', 'age':30 , 'address' : 'US, okland'})  # 키의 개수와 값이 같아야함


## **를 두번 사용하는 이유
personal_info(*x)   # 키가 출력됨


## 키워드 인수를 사용하는 가변 인수 함수 만들기
# * 함수이름(**매개변수)
   # 코드

def personal_info(**kwargs):
    for kw, arg in kwargs.items():
        print(kw, ': ', arg, sep='')

def personal_info(**kwargs):
    if 'name' in kwargs:
        print('이름: ', kwargs['name'])
    if 'age' in kwargs:
        print('나이: ', kwargs['age'])
    if 'address' in kwargs:
        print('주소: ', kwargs['adreess'])

# 참고 고정인수와 가변인수를 함께 사용하기
def personal_info(name, **kwargs)

# 참고 위치 인수와 키워드 인수를 함께 사용하기
def custum_print(*args, ** kwargs):


### 매개변수에 초깃값 지정하기

# def 함수이름(매개변수=값)
  # 코드

def personal_info(name, age, address='비공개')    # 항상 마지막에 줘야함. 1, 3 이렇게 주면 에러남
    


