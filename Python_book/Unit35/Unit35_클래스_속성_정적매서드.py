#### 클래스 속성과 정적, 클래스 메서드 사용하기

## 클래스 속성 사용하기
# class 클래스 이름:
  # 속성 = 값

class Person():
    bag = []

    def put_bag(self, stuff):
        self.bag.append(stuff)   # self는 현재 인스턴스를 뜻하므로 클래스 속성을 지칭하기에는 조금 모호함
                                 # 그러므로 self를 클래스 이름으로 바꾸어주면 좀 더 명확해짐
    def put_bag(self, stuff):
        Person.bag.append(stuff)

lebron = Person()
lebron.put_bag('공')

stephen = Person()
stephen.put_bag('신발')

print(lebron.bag)
print(stephen.bag)       # 각각 다르게 넣었는데 결과는 같아짐


# 참고 속성, 메서드 이름을 찾는 순서
# 인스턴스 -> 클래스 순으로 찾음. 인스턴스 속성이 없으면 클래스 속성을 찾게 됨
# 인스턴스와 클래스에서 __dict__ 속성을 출력해 보면 현재 인스턴스와 클래스의 속성을 딕셔너리로 확인할 수 있음


## 인스턴스 속성 사용하기
class Person:
    def __init__(self):
        self.bag = []

    def put_bag(self,stuff):
        self.bag.append(stuff)

lebron = Person()
lebron.put_bag('나이키')

stephen = Person()
stephen.put_bag('언더아머')

print(lebron.bag)
print(stephen.bag)

## 비공개 클래스 속성 사용하기
class Knight:
    __item_limit = 10

    def print_item_limit(self):
        print(Knight.__item_limit)

x = Knight()
x.print_item_limit()
print(Knight.__item_limit) # 밖에서는 접근 안됨


# 참고 클래스와 메서드의 독스트링 사용하기
# """ """ 또는 ''' ''' 으로 사용 가능
class Person:
    '''사람 클래스입니다.'''

    def greeting(self):
        '''인사 메서드입니다.'''
        print('Hello')


print(Person.__doc__)  # 사람 클래스입니다.
print(Person.greeting.__doc__)  # 인사 메서드입니다.

maria = Person()
print(maria.greeting.__doc__)  # 인사 메서드입니다.



### 정적 메서드 사용하기
#
# 지금까지 클래스의 메서드를 사용할 때 인스턴스를 통해서 호출했습니다.
# 이번에는 인스턴스를 통하지 않고 클래스에서 바로 호출할 수 있는
# 정적 메서드와 클래스 메서드에 대해 알아보겠습니다.
#
# 먼저 정적 메서드입니다. 정적 메서드는 다음과 같이 메서드
# 위에 @staticmethod를 붙입니다. 이때 정적 메서드는 매개변수에 self를 지정하지 않습니다.

# class 클래스이름:
#     @staticmethod
#     def 메서드(매개변수1, 매개변수2):
#         코드

# @staticmethod처럼 앞에 @이 붙은 것을 데코레이터라고 하며
# 메서드(함수)에 추가 기능을 구현할 때 사용합니다.

class Calc:
    @staticmethod
    def add(a, b):
        print(a + b)

    @staticmethod
    def mul(a, b):
        print(a * b)

Calc.add(10, 20)
Calc.mul(20 , 30)

# 참고 | 파이썬 자료형의 인스턴스 메서드와 정적 메서드
# 파이썬의 자료형도 인스턴스 메서드와 정적, 클래스 메서드로 나뉘어져 있습니다.
# 예를 들어 세트에 요소를 더할 때는 인스턴스 메서드를 사용하고, 합집합을 구할 때는 정적 메서드를 사용하도록 만들어져 있습니다.
#
# >>> a = {1, 2, 3, 4}
# >>> a.update({5})    # 인스턴스 메서드
# >>> a
# {1, 2, 3, 4, 5}
# >>> set.union({1, 2, 3, 4}, {5})    # 정적(클래스) 메서드
# {1, 2, 3, 4, 5}
# 이처럼 인스턴스의 내용을 변경해야 할 때는 update와 같이 인스턴스 메서드로 작성하면 되고,
# 인스턴스 내용과는 상관없이 결과만 구하면 될 때는 set.union과 같이 정적 메서드로 작성하면 됩니다.



### 클래스 메서드 사용하기
class Person:
    count = 0           # 클래스 속성

    def __init__(self):
        Person.count += 1 # 인스턴스가 만들어질 때 클래스 속성 count에 1을 더함


    @classmethod
    def print_count(cls):           # cls로 클래스 속성에 접근
        print('{0}명 생성되었습니다.'.format(cls.count))

lebron = Person()
stephen = Person()

Person.print_count()

# 35.5 연습문제: 날짜 클래스 만들기
# 다음 소스 코드에서 Date 클래스를 완성하세요.
# is_date_valid는 문자열이 올바른 날짜인지 검사하는 메서드입니다.
# 날짜에서 월은 12월까지 일은 31일까지 있어야 합니다.
# practice_class_static_class_method.py


class Date:
    @staticmethod
    def is_date_valid(date_string):
        year, month, day = map(int, input(date_string.split('-')))
        return day <= 31 and month <= 12


if Date.is_date_valid('2000-10-31'):
    print('올바른 날짜 형식입니다.')
else:
    print('잘못된 날짜 형식입니다.')