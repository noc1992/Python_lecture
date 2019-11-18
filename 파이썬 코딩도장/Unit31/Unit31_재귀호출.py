#### 함수에서 재귀호출 사용하기

### 재귀호출 사용하기
def hi:
    print('hi')
    hi()             #무한 루프 발생


## 재귀호출에 종료조건 만들기
def hi(count):
    if count == 0:
        return

    print('hi, wordl!', count)

    count -= 1
    hi(count)

hi(8)


### 재귀호출로 팩토리얼 구하기
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n -1)

# 참고 등차수열
def ari_seq(n, d):
    if n == 1:
        return 1
    return ari_seq(n-1, d) + d

