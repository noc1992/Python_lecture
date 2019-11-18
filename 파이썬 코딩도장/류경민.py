# 3번
# 두개의 정수를 입력받아 작은수에서부터 큰수까지(큰수 포함)홀수의 합을 구해서 출력하는 프로그램을 for로 작성
a, b = map(int, input().split())
1 9

c = []
if a > b:
    for i in range(b, a - b + 2):
        if i % 2 == 1:
            c.append(i)
    print(sum(c))
else:
    for i in range(a, b - a + 2):
        if i % 2 == 1:
            c.append(i)
    print(sum(c))


# 4번
# 연 복리 이자율을 입력받아(단위 %) 원금이 2배가 되는데 최소 몇년이 걸리는지 알아보는 프로그램
# while로 작성

a, b = map(float, input().split())
2.5 5000

c =[]
year = 0
while True:
    d = b * a * 1/100
    year += 1
    c.append(d)
    sum(c)
    if sum(c) > b:
        print(year, "년")
        break


# 5번
# bts리스트가 주어졌을때 아래와 같은 답이 나오도록 print문을 작성
bts = ['RM','진','슈가','제이홉','지민','뷔', '정국']

# 1) 뷔
print("뷔")

# 2) ['RM']
print(bts[0:1])

# 3) ['뷔', '정국']
print(bts[len(bts)-2:len(bts)])

# 4) ['슈가','제이홉','지민']
print(bts[2:5])

# 5) ['RM', '슈가','지민','정국']
print(bts[0:len(bts):2])



# 6번
# 다음과 같은 딕셔너리 vegetables가 주어졌을 때, 아래 그림과 같이 가격이 높은 것부터 내림차순으로 출력하는 프로그램을 작성하되
# 가격은 길이를 7로 만들고 1000단위,를 찍은 뒤 우측정렬 하시오.
vegetables = {'가지':800, '오이':600, '수박':15000,'호박':1000, '깻잎':500}

a = sorted(vegetables.values(),reverse=True)
{key:a for keys in vegetables.fromkeys(key).keys()}
for key, value in a:



# 7번

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


maxNum = 0
for i in range(100, 1000):
    for k in range(i, 1000):
        if is_palindrome(str(i * k)):
            if i * k > maxNum:
                maxNum = i * k
                maxA = i
                maxB = k
print(maxNum, maxA, maxB)



# 9번
a = [1, 3, 5, 7, 9]

b = list(map(lambda x: x * x, a))