#### 클래스 상속 사용하기

### 사람 클래스로 학생클래스 만들기
class Person:
    def greeting(self):
        print('안녕하세요.')

class Student(Person):
    def study(self):
        print('공부하기')

stephen = Student()
stephen.greeting()
stephen.study()

issubclass(Student, Person)  # 상속된 클래스 인지 확인하기



### 상속관계와 포함 관계 알아보기


## 상속 관계
class Person:
    def greeting(self):
        print('안녕하세요.')


class Student(Person):
    def study(self):
        print('공부하기')


## 포함 관계
class Person:
    def greeting(self):
        print('안녕하세요')

class PersonList:
    def __init__(self):
        self.person_list = []               # 리스트 속성에 Person 인스턴스를 넣어서 관리

    def append_person(self, person):
        self.person_list.append(person)    # 리스트 속성에 Person 인스턴스를 추가하는 함수



### 기반 클래스의 속성 사용하기

## super()로 기반 클래스 초기화 하기
class Person:
    def __init__(self):
        print('Person __init__')
        self.hi = 'hi'

class Student(Person):
    def __init__(self):
        print('Student __init__')
        super().__init__()
        self.school = '파이썬 코딩 도장'

stephen = Student()
print(stephen.school)
print(stephen.hi)


## 기반 클래스를 초기화 하지 않아도 되는 경우
# 만약 파생 클래스에서 __init__ 메서드를 생략한다면 기반 클래스의 __init__이 자동으로 호출되므로 super()는 사용하지 않아도 됩니다.

class Person:
    def __init__(self):
        print('Person __init__')
        self.hi = '안녕하세요'

class Student(Person):
    pass

stephen = Student()
print(stephen.hi)


### 메서드 오버 라이딩 사용하기

class Person:
    def greeting(self):
        print('안녕하세요.')


class Student(Person):
    def greeting(self):
        super().greeting()  # 기반 클래스의 메서드 호출하여 중복을 줄임
        print('저는 파이썬 코딩 도장 학생입니다.')


james = Student()
james.greeting()


### 다중 상속 사용하기

class Person:
    def greeting(self):
        print('안녕하세요.')

class University:
    def manage_credit(self):
        print('학점관리')

class Undergraduate(Person, University):
    def study(self):
        print('공부하기')

stephen = Undergraduate()
stephen.greeting()           # 안녕하세요.: 기반 클래스 Person의 메서드 호출
james.manage_credit()        # 학점 관리: 기반 클래스 University의 메서드 호출
james.study()                # 공부하기: 파생 클래스 Undergraduate에 추가한 study 메서드


## 다이아몬드 상속

class A:
    def greeting(self):
        print('안녕하세요. A입니다.')


class B(A):
    def greeting(self):
        print('안녕하세요. B입니다.')


class C(A):
    def greeting(self):
        print('안녕하세요. C입니다.')


class D(B, C):
    pass


x = D()
x.greeting()  # 안녕하세요. B입니다.


### 추상 클래스 사용하기

from abc import *

class StudentBase(metaclass=ABCMeta):
    @abstractclassmethod
    def study(self):
        pass

    @abstractclassmethod
    def go_to_school(self):
        pass

class Student(StudentBase):
    def study(self):
        print('공부하기')

    def go_to_school(self):
        print('학교가기')

stephen = Student()
stephen.study()
stephen.go_to_school()