#### 람다 표현식 사용하기

### 람다 표현식으로 함수 만들기
def plus_ten(x):
    return x + 10

lambda x: x + 10

plus_ten = lambda x: x + 10

## 람다 표현식 자체 호출
(lambda x: x + 10)(1)


## 람다 표현식 안에서는 변수를 만들 수 없다.
(lambda x: y = 10; x + y)(1)         # 안됨


## 람다 표현식을 인수로 사용하기
def plus_ten(x):
    return  x + 10

list(map(plus_ten, [1, 2, 3]))
list(map(lambda x: x + 10, [1, 2, 3]))   # 람다식은 함수 이름이 들어갈 자리에


### 람다 표현식과 map, filter,reduce 함수 활용하기

## 람다 표현식에 조건부 표현식 사용하기
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(map(lambda x: str(x) if x % 3 == 0 else x, a))     # if를 사용했다면 반드시 else를 사용해야함
list(map(lambda x: str(x) if x == 1 else float(x) if x == 2 else x + 10, a))

# 차라리 이걸써!
def f(x):
    if x == 1:
        return str(x)
    elif x == 2:
        return float(x)
    else:
        return  x + 10


list(map(f, a))


## map에 객체를 여러 개 넣기
a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]
list(map(lambda x, y: x * y, a, b))


## filter 사용하기
# * filter(함수, 이터레이터)
def f(x):
    return x > 5 and x < 10

a =  [6, 1, 2, 7, 11, 144, 0, 5]

list(filter(f, a))
list(filter(lambda x: 5 < x <10, a))


## reduce 사용하기
