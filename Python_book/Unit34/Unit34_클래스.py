#### 클래스 만들기

class Person:                        # 클래스 이름 첫글자 대문자
    def greeting(self):              # 함수와 다른점은 self
        print('greetings!')

stephen = Person()
stephen.greeting()


## 파이썬에서 흔히 볼 수 있는 클래스
# int list dict 자료형 등도 모두 클래스 입니다.


## 인스턴스와 객체의 차이점
# 사실 인스턴스와 객체는 같은 것을 뜻한다. 보통 객체만 지칭할 떄는 그냥 객체라고 부른다.
# 하지만 클래스와 연관지어서 말할때는 인스턴스 라고 부른다.

a = list(range(10))   # a , b 는 객체
b = list(range(20))   # 그리고 a, b 는 클래스의 인스턴스!

# 참고 빈 클래스 만들기
# class Person():
   # pass

# 참고 메서드 안에서 메서드 호출하기
# self.메서드()
# class Person:
#     def greeting(self):
#         print('Hello')
#
#     def hello(self):
#         self.greeting()  # self.메서드() 형식으로 클래스 안의 메서드를 호출
#
#
# james = Person()
# james.hello()  # Hello

# 참고 | 특정 클래스의 인스턴스인지 확인하기
# 현재 인스턴스가 특정 클래스의 인스턴스인지 확인할 때는 isinstance 함수를 사용합니다. 특정 클래스의 인스턴스가 맞으면 True, 아니면 False를 반환합니다.
#
# isinstance(인스턴스, 클래스)
#
# >>> class Person:
# ...     pass
# ...
# >>> james = Person()
# >>> isinstance(james, Person)
# True
# isinstance는 주로 객체의 자료형을 판단할 때 사용합니다.
# 예를 들어 팩토리얼 함수는 1부터 n까지 양의 정수를 차례대로 곱해야 하는데,
# 실수와 음의 정수는 계산할 수 없습니다. 이런 경우에 isinstance를 사용하여 숫자(객체)가 정수일 때만 계산하도록 만들 수 있습니다.
#
# def factorial(n):
#     if not isinstance(n, int) or n < 0:    # n이 정수가 아니거나 음수이면 함수를 끝냄
#         return None
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)



### 속성 사용하기

class Person():
    def __init__(self):
        self.hi = 'greetings!'

    def  greeting(self):
        print(self.hi)

stephen = Person()
stephen.greeting()


## self의 의미
# 인스턴스 자기 자신을 의미한다.

## 인스턴스를 만들때 값 받기
# Class Person:
 # def __init__(self, name, age, address):
      # self.hi = 'greetings!!'
      # self.name = name
      # self.age = age
      # self.address = address

      #def greeing(self):
      # print('{0} 저는 {1} 입니다. '.format(self.hi, self.name))

#  maria = Person('마리아', 20 , '서울 서초구 반포동')

# print('이름:', maria.age)
# print('나이:', maria.name)
# print('주소:', maria.address)


# 참고 클래스의 위치 인수 키워드 인수
# 클래스로 인스턴스를 만들 때 위치 인수와 키워드 인수를 사용할 수 있습니다.
# 언패킹 시 *args를 사용하면 됩니다.
class Person():
    def __init__(self, *args):
        self.name = args[0]
        self.age = args[1]
        self.address = args[2]

stephen = Person(*['스테픈', '32', 'San francisco'])

# 언패킹 시
class Person:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.age = kwargs['age']
        self.address = kwargs['address']

stephen1 = Person(name='stephen', age='32', address='oakland, San Francisco')
stephen2 = Person(**{'name': 'stephen', 'age': 32, 'address':'oakland, San Francisco'})

# 참고 인스턴스를 생성한 뒤에 속성 추가하기, 특정 속성만 허용하기
class Person:
    pass

stephen = Person()
stephen.name = '스테픈'
stephen.name            # 이렇게 추가된 속성은 해당 인스턴스에만 생성됨 다른데에는 없음

# 인스턴스는 생성한 뒤에 속성을 추가할 수 있으므로 __init__ 메서드가 아닌 다른 메서드에서도
# 속성을 추가할 수있습니다. 단 이때는 메서드를 호출해야 속성이 됩니다.
class Person():
    def greeting(self):
        self.hi = '안녕하세요'

stephen = Person()
stephen.greeting()   # 반드시 호출을 해야 불러올수 있음
stephen.hi


# 속성 제한   __slots__=['속성이름1, '속성이름2']
class Person:
    __slots__ = ['name', 'age']         # name age만 허용(다른 속성은 제한)

stephen = Person()
stephen.name = '스테픈'                      # 허용
stephen.age = 32                            # 허용
stephen.address = 'oakland, San Francisco'  #허용되지 않은 속성이기에 에러가 남


### 비공개 속성 사용하기
class Person():
    def __init__(self, name, age, address, money):
        self.name = name
        self.age = age
        self.address = address
        self.__money = money

    def pay(self, amount):
        if amount > self.__money:
            print('off the balance!!')
            return
        self.__money -= amount
        print('balance : {0}'.format(self.__money))


stephen = Person('스테픈', '32', 'Oakland', 1000000000000)
stephen.pay(30000000)     # 비공개 속성이기 때문에 에러가 남


# 참고 비공개 메서드
class Person():
    def __greeting(self):
        print('hi')

    def hi(self):
        self.__greeting()   # 메서드 앞에 __을 붙여주면 가능

stephen = Person()
stephen.__greeting()    # 클래스 밖에서는 비공개 메서드 호출 안됨


## 연습문제 : 게임 케릭터 클래스 만들기
class Knight():
    def __init__(self, h_p, mana, armor, attack):
        self.h_p = h_p
        self.mana = mana
        self.armor = armor
        self.attack = attack

    def slash(self):
        print('베기 {0}'.format(self.attack))

x = Knight(h_p=542.4, mana=210.3, armor=38, attack= 300)
print(x.h_p, x.mana, x.armor)
x.slash()
