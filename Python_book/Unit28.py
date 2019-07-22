#### 회문 판별하기

### 반복문으로 문자 검사하기

word = input('단어를 입력: ')

is_pali = True

for i in range(len(word) // 2):          # 회문 판별값을 저장할 변수, 초깃값 true
    if word[i] != word[-1 -i]:           # 0부터 문자열 길이의 절반만큼 반복
        is_pali = False                  # 왼쪽 문자와 오른쪽 문자를 비교하여 문자가 다르면
        break                            # 회문 아님

print(is_pali)


## 시퀸스 뒤집기로 문자 검사
word = input('단어: ')
level
print(word == word[::-1])


## 리스트와 reversed 사용하기
word = 'level'
list(word) == list(reversed(word))


## 문자열의 join 메서드와 reversed 사용하기
word == ''.join(reversed(word))



### N-gram 만들기

## 반복문으로 N-gram 출력하기
text = 'hidear'
for i in range(len(text) - 1):            # 2-gram 이므로 문자열의 끝에서 한 글자 앞까지만 반복
    print(text[i], text[i + 1], sep='')   # 현재 문자와 그 다음 문자 출력


text = 'this is sparta!'
word = text.split()
for i in range(len(word) - 1):
    print(word[i], word[i + 1])


## zip 으로 2-gram 만들기
text = 'this is sparta'
txt = text.split()
two_gram = zip(txt, txt[1:])
print(two_gram)
for i in two_gram:
    print(i[0], i[1], sep='')

list(zip(txt[:]))

list(zip(txt, txt[1:]))

list(txt[:])


## zip과 리스트 표현식으로 N-gram 만들기
text = 'sparta'
[text[i:] for i in range(3)]

# zip에 리스트의 각 요소를 콤마로 구분해서 넣어 주려면 리스트 앞에 *를 붙여야함
list(zip(*['sparta', 'parta', 'arta']))

list(zip(*[text[i:] for i in range(3)]))



### 연습문제 : 단어 단위 n-gram 만들기
n = int(input())
7
text = input()
Python is a programming language that lets you work quickly
words = text.split()
list(zip(*[words[i:] for i in range(n)]))
if len(words) < n:
    print('wrong')
else:
   n_g = zip(*[words[i:] for i in range(n)])
   for i in n_g:
       print(i)