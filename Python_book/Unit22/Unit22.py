#### 리스트 조작하기

### 리스트 조작하기

## 리스트에 요소 추가하기
# * append: 요소 하나를 추가
# * extend: 리스트를 연결하여 확장
# * insert: 특정 인덱스에 요소 추가

## 리스트에 요소 하나 추가
a = [10, 20, 30]
a.append(500)
len(a)
a= []      # 빈리스트
a.append(10)

## 리스트 안에 리스트 추가하기
a.append([23, 13 , 100])
a

## 리스트 확장하기
b = [1,2,3]
b.extend([300, 100])
len(b) # 5나옴

## 리스트의 특정 인덱스에 요소 추가하기
b.insert(3,77)
# insert의 패턴
b.insert(0, 200)  # 맨처음에 요소 추가
b.insert(len(b), 90) # 리스트의 끝에 요소 추가

# 리스트 중간에 요소 여러개를 추가
b[2:2] = [1,332]

## 리스트에서 요소삭제
pop : 마지막 요소 또는 특정 인덱스의 요소 삭제
remove : 특정 값을 찾아서 삭제

## 리스트에서 특정 인덱스의 요소를 삭제하기
a.pop()
a.pop(1)
del a[0]

## 리스트에서 특정값을 찾아서 삭제
a.remove(30)
b.remove(1)   # 만약 값이 여러개라면 처음 값 삭제

## 리스트에서 특정 값의 인덱스 구하기
a = [10, 20, 30, 14, 11, 10]
a.index(10)      # 중복있을 경우 첫번째만

## 특정 값의 개수 구하기
a = ['append','c', 'command', 'cop', 'city']
a.count('c')


## 리스트의 순서를 뒤집기
a.reverse()

## 리스트의 요소를 정렬하기
# * sort() 또는 sort(reverse=False): 리스트의 값을 작은 순서대로 정렬
# * sort(reverse=True): 리스트의 값을 큰 순서대로 정렬
b.sort(reverse=False)

## 리스트의 모든 요소 삭제
b.clear()
del a[:]

## 리스트를 슬라이스로 조작하기
a = [10, 20,30]
a[len(a):] = [500]   # 이 리스트의 끝에서 뭔가 시작하겠다! 하나추가시 a.append 와 같음
a[len(a):] = [300, 100]  # a.extend와 같음

# 참고
리스트가 비어있는지 확인하기
if not len(b):
if len(b):

if not b:
if b:

if a:
    print(a[-1])  # 리스트가 비어있을시 에러가 남


###리스트의 할당과 복사
a = [1, 2, 3, 4]
b = a       # 복사 될 것 = 복사 할 것

a is b # 이름만 다를뿐 같은 객체
b[2] = 99 # 모두 반영

b = a.copy() # 완전히 다른 객체로 만드려면
a is b # false
a == b # True 요소는 같기 때문, 그러나 값을 넣으면 넣은 객체만 추가됨


### 반복문으로 리스트의 요소를 모두 출력하기

## for 반복문으로 요소 출력하기
# for 변수 in 리스트:
#     코드
for i in a:
    print(a)

## 인덱스와 요소를 함께 출력하기
# for 인덱스, 요소 in enumerate(리스트):
for index, value in enumerate(a):
    print(index + 1, value)   # 1부터 출력하고 싶을때

for index, value in enumerate(a, start=1): # enumerate(a, 1)로 줄이기 가능
    print(index, value)

# for 반복문에서 인덱스로 요소 출력하기
for i in range(len(a)):
    print(a[i])

## while 반복문으로 요소 출력하기
i = 0
while i < len(a):  #만약 i <= len(a)처럼 <=을 사용하면 리스트의 범위를 벗어나게 되므로 주의해야 합니다.
    print(a[i])
    i += 1

### 리스트의 가장 작은수 큰수 구하기
smallest = a[0]
largest = a[0]
for i in a:
    if i < smallest:
        smallest = i
    if i > largest:
        largest = i
smallest
largest

b = [5, 1, 32, 17, 100, 3]
b.sort()
b[0]
b.sort(reverse=True)
b[0]

min(b)
max(b)

## 요소의 합계 구하기
x=0
for i in a:
    x += i

sum(a)

### 리스트 표현식 사용하기
# * [식 for 변수 in 리스트]
# * list(식 for 변수 in 리스트)
a = [i + b[i] for i in range(10)]
b = list(i * 4 for i in range(10))

## 리스트 표현식에서 if 조건문 사용하기
# * [식 for 변수 리스트 if 조건식]
# * list(식 for 변수 in 리스트 if 조건식)
a = [i for i in range(10) if i % 2 ==0]

## for 반복문과 if 조건문을 여러번 사용하기
a = [i * j for j in range(2, 10) for i in range(1, 10)]

b = [i * j for j in range(2,10)
           for i in range(1,10)]  # 리스트 표현식에 for가 여러 개일 때 처리 순서는 뒤에서 앞으로 순입니다.

### 리스트에 map 사용하기
# * list(map(함수, 리스트))
# * tuple(map(함수, 튜플))

a = [1.2, 2.5, 3.5, 7.7]
for i in range(len(a)):
    a[i] = int(a[i])

a = list(map(int, a))

a = list(map(str, range(10)))


## input().split() 과 map
a = input().split()   # 문자열이 만들어짐
10 20

x = input().split()    # input().split()의 결과는 문자열 리스트
m = map(int, x)        # 리스트의 요소를 int로 변환, 결과는 맵 객체
a, b = m               # 맵 객체는 변수 여러 개에 저장할 수 있음

### 튜플 응용하기

##튜플에서 특정 값의 인덱스 구하기
a = (34, 21, 42, 77, 12)
a.index(77)

## 특정 값의 개수 구하기
b = ('c', 'cop', 'capital')
b.count('c')


## for 반복문으로 요소 출력하기
c = ('my prof must give me adjustment for grade c')
for i in c:
    print(i, end='')

## 튜플 표현식 사용하기
# * tuple(식 for 변수 in 리스트 if 조건식)
a = tuple(i for i in range(10) if i % 2 == 0)

## tuple 에 map 사용하기
a = tuple(map(int, a))
a

## 튜플에서 작은수 큰수 합계
min(a)
max(a)
sum(a)