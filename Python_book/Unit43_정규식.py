#### 정규 표현식 사용하기

### 문자열 판단하기

import re

re.match('greeting', 'greeting! ladies and gentelman')  #<re.Match object; span=(0, 8), match='greeting'>


## 문자열이 맨 앞에 오느지 맨 뒤에 오는지 판단하기
re.search('^greetings', 'greetings! ladies')
re.search('world!$', 'Hello, world!')


## 지정된 문자열이 하나라도 포함되는지 판단하기
re.match('hi|greeting', 'hi! greetings! 안녕하세요')



### 범위 판단하기
re.match('[0-9]*', '98123a1')
re.match('a*b','b')
re.match('a*b','bab')
re.match('a+b','abb')


## 문자가 한개만 있는지 판단하기
re.match('H', 'H')
re.match('H.', 'Hi!')


## 문자의 개수 판단하기
re.match('h{3}', 'hhh')

re.match('[0-9]{3}-[0-9]{4}','909-1234')


## 숫자와 영문 문자를 조합해서 판단하기
re.match('[a-zA-Z0-9]', 'Hiho1234')
re.match('[가-힣]', '홍길동')


## 특정문자 범위에 포함되지 않는지 판단하기
re.match('[^A-Z]+', 'Heoo')          # 대문자를 제외. 대문자가 있으므로 패턴에 매칭되지 않음
>>> re.match('[^A-Z]+', 'hello')     # 대문자를 제외. 대문자가 없으므로 패턴에 매칭됨
re.match('[^A-Z]+', 'heoo')


re.search('^[A-Z]+', 'Hehigo')   # 대문자로 시작하므로 패턴에 매칭됨

re.search('[0-9]+$', 'HOhohi3')  # 숫자로 끝나므로 패턴에 매칭됨


## 특수 문자 판단하기
re.search('\*+', '1 ** 2E')                 # *이 들어있는지 판단
re.match('[$()a-zA-Z0-9]+', '$(document)')  # $, (, )와 문자, 숫자가 들어있는지 판단

# \d: [0-9]와 같음. 모든 숫자
# \D: [^0-9]와 같음. 숫자를 제외한 모든 문자
# \w: [a-zA-Z0-9_]와 같음. 영문 대소문자, 숫자, 밑줄 문자
# \W: [^a-zA-Z0-9_]와 같음. 영문 대소문자, 숫자, 밑줄 문자를 제외한 모든 문자

>>> re.match('\d+', '1234')          # 모든 숫자이므로 패턴에 매칭됨
<_sre.SRE_Match object; span=(0, 4), match='1234'>
>>> re.match('\D+', 'Hello')         # 숫자를 제외한 모든 문자이므로 패턴에 매칭됨
<_sre.SRE_Match object; span=(0, 5), match='Hello'>
>>> re.match('\w+', 'Hello_1234')    # 영문 대소문자, 숫자, 밑줄 문자이므로 패턴에 매칭됨
<_sre.SRE_Match object; span=(0, 10), match='Hello_1234'>
>>> re.match('\W+', '(:)')    # 영문 대소문자, 숫자, 밑줄문자를 제외한 모든 문자이므로 패턴에 매칭됨
<_sre.SRE_Match object; span=(0, 3), match='(:)'>


## 공백 처리하기
# \s: [ \t\n\r\f\v]와 같음. 공백(스페이스), \t(탭) \n(새 줄, 라인 피드), \r(캐리지 리턴), \f(폼피드), \v(수직 탭)을 포함
# \S: [^ \t\n\r\f\v]와 같음. 공백을 제외하고 \t, \n, \r, \f, \v만 포함

>>> re.match('[a-zA-Z0-9 ]+', 'Hello 1234')     # ' '로 공백 표현
<_sre.SRE_Match object; span=(0, 10), match='Hello 1234'>
>>> re.match('[a-zA-Z0-9\s]+', 'Hello 1234')    # \s로 공백 표현
<_sre.SRE_Match object; span=(0, 10), match='Hello 1234'>



### 그룹 사용하기

# * (정규표현식)(정규표현식
m = re.match('([0-9]+) ([0-9]+)', '10 295')

# 매치객체.group(그룹 숫자)
m.group(1)     # 첫 번째 그룹(그룹 1)에 매칭된 문자열을 반환
m.group(2)     # 두 번째 그룹(그룹 2)에 매칭된 문자열을 반환
m.group()      # 매칭된 문자열을 한꺼번에 반환
m.group(0)     # 매칭된 문자열을 한꺼번에 반환

# 매치객체.groups()
m.groups()   # 각 그룹에 해당하는 문자열 튜플형태로 반환


# (?P<이름>정규표현식)
m = re.match('(?P<func>[a-zA-Z_][a-zA-Z0-9_]+)\((?P<arg>\w+)\)', 'print(1234)')
m.group('func')  # 그룹 이름으로 매칭된 문자열 출력

m.group('arg')   # 그룹 이름으로 매칭된 문자열 출력


## 패턴에서 매칭되는 모든 문자열 가져오기
re.findall('[0-9]+', '1 2 Fizz 4 Buzz Fizz 7 8')

# 참고 * + dhk 그룹 활용하기
>>> re.match('[a-z]+(.[a-z]+)*$', 'hello.world')    # .world는 문자열이므로 패턴에 매칭됨
<_sre.SRE_Match object; span=(0, 11), match='hello.world'>
>>> re.match('[a-z]+(.[a-z]+)*$', 'hello.1234')     # .1234는 숫자이므로 패턴에 매칭되지 않음
>>> re.match('[a-z]+(.[a-z]+)*$', 'hello')          # .뒤에 문자열이 없어도 패턴에 매칭됨
<_sre.SRE_Match object; span=(0, 5), match='hello'>


### 문자열 바꾸기

# re.sub('패턴', '바꿀문자열', '문자열', 바꿀횟수)
re.sub('app|original', 'fruit', 'app is original way')  # app 또는 original 을 fruit으로 바꿈

re.sub('[0-9]+', 'n', '1 2 Fizz 4 Buzz Fizz 7 8')    # 숫자만 찾아서 n으로 바꿈


# 교체함수(매치객체)
# re.sub('패턴', 교체함수, '문자열', 바꿀횟수)

def multiple10(m):
    n = int(m.group())     # 매칭된 문자열을 가져와서 정수로 변환
    return str(n * 10)     # 숫자에 10을 곱한뒤 문자열로 변환

re.sub('[0-9]+', multiple10, '1 2 Fizz 4 Buzz 78')


## 찾은 문자열을 결과에 다시 사용하기
re.sub('([a-z]+) ([0-9]+)', '\\2 \\1 \\2 \\1', 'hello 1234') # 그룹 2,1,2,1 순으로 바꿈

re.sub('({\s*)"(\w+)":\s*"(\w+)"(\s*})', '<\\2>\\3</\\2>', '{ "name": "james" }')


# 만약 그룹에 이름을 지었다면 \\g<이름> 형식으로 매칭된 문자열을 가져올 수 있습니다(\\g<숫자> 형식으로 숫자를 지정해도 됩니다).

re.sub('({\s*)"(?P<key>\w+)":\s*"(?P<value>\w+)"(\s*})', '<\\g<key>>\\g<value></\\g<key>>', '{ "name": "james" }')


# 참고 | raw 문자열 사용하기
# 정규표현식의 특수 문자를 판단하려면 \를 붙여야 합니다.
# 여기서 문자열 앞에 r을 붙여주면 원시(raw) 문자열이 되어 \를 붙이지 않아도 특수
# 문자를 그대로 판단할 수 있습니다. 따라서 raw 문자열에서는 \\숫자, \\g<이름>, \\g<숫자>는 \숫자,
# \g<이름>, \g<숫자> 형식처럼 \를 하나만 붙여서 사용할 수 있습니다.
#
# r'\숫자 \g<이름> \g<숫자>'
#
# >>> re.sub('({\s*)"(\w+)":\s*"(\w+)"(\s*})', r'<\2>\3</\2>', '{ "name": "james" }')
# '<name>james</name>'

