#### 문자열 응용하기

### 문자열 조작하기

## 문자열 바꾸기
"hi! python!".replace('hi', 'greatings')
s = "안녕하세요. 저는 너무 힘이 듭니다"
s = s.replace("듭니다", "납니다")
s

## 문자 바꾸기
table = str.maketrans('aerdr', '12345')       # 길이가 같아야 한데
'airodinaymic'.translate(table)

## 문자열 분리하기
'apple pear grape'.split()
'apple, mellon, water'.split(', ')


## 구분자 문자열과 문자열 리스트 연결하기
' '.join(['apple', 'pear', 'grape'])
'-'.join(['apple', 'pear', 'grape'])


## 소문자를 대문자로
'a'.upper()

## 대문자를 소문자로
'B'.lower()


## 왼쪽 공백 삭제하기
'   ㅔㄴㅇㄹ   '.lstrip()

## 오른쪽 공백 삭제하기
'   ㅁㄴㅇㄹ   '.rstrip()

## 양쪽 공백 삭제하기
' ㅁㄴㄷㄱ  '.strip()

## 왼쪽 특정 문자 삭제하기/ 오른쪽 / 양쪽
',.ㅁㄴㅇㄹㄴㄷㄺ'.lstrip('.,')
',.ㄴㄹㄴㄷㄹㄴㅇ.,'.rstrip(',.')
',.sdfsef,.'.strip(',.')

# 참고
구두점 간단히 제거
import string
with open('hello.txt', 'r') as file:
    for line in file:
        print(line.strip('\n'))

line.split()

### 문자열 서식 지정자와 포매팅 사용하기

## 서식 지정자로 문자열 넣기
'i an %s.'  % 'Ryuky'   # s는 스트링
name = 'Ryuky'
'i am a %s.' % name

## 서식 지정자로 숫자 넣기
'i am %d.' % 28   # d 는 숫자


##서식 지정자로 소수점 표현하기
'%f' % 2.4                 # 실수는 f
'%.2f'  % 2.3455           # 숫자는 자리수


## 서식 지정자로 문자열 정렬하기
'%10s' % 'python'     ## 앞에 공백이 4칸 생김
'%-10s' % 'asdf'      ## 뒤에 공백 생김


## 서식 지정자로 문자열 안에 값 여러개 넣기
'Today is %d %s.' % (3, 'fuc')

## format 메서드 사용하기
# * '{인덱스}'.format(값)
'hi, {0}'.format('world')
'hi, {0}'.format(10)


## format 메서드로 값을 여러개 넣기
'hi, {0} {3} {1} {2}'.format('hi','ho','ho','man')

## format 메서드로 같은 값을 여러개 넣기
'{0} {1} {0} {0}'.format('do', 'i really suck')

## format 메서드에서 인덱스 생략
'hi {} {} {}'.format('y', 't', 'a')  ## 순서대로

## format 메서드에서 인덱스 대신 이름 지정하기
'Hello, {language} {version}'.format(language='Python', version=3.6)

## 문자열 포매팅에 변수를 그대로 사용하기
l = 'py'
ver = 2.7
f'hi, {l} {ver}'
# 중괄호 출력
'{{ {0} }}'.format('pu')


## format 메서드로 문자열 정렬하기




# 참고 | 금액에서 천단위로 콤마 넣기
# 숫자 중에서 금액은 천단위로 ,(콤마)를 넣죠? 파이썬에서는 간단하게 천단위로 콤마를 넣을 수 있습니다.
#
# 먼저 format 내장 함수를 사용하는 방법입니다. 다음과 같이 format 함수에 숫자와 ','를 넣어줍니다.
#
# format(숫자, ',')
#
# >>> format(1493500, ',')
# '1,493,500'
# format 함수는 서식 지정자와 함께 사용할 수 있습니다. 다음은 콤마를 넣은 숫자를 오른쪽 정렬합니다.
#
# >>> '%20s' % format(1493500, ',')    # 길이 20, 오른쪽으로 정렬
# '           1,493,500'
# 포매팅에서 콤마를 넣으려면 다음과 같이 :(콜론)뒤에 ,(콤마)를 지정하면 됩니다.
#
# >>> '{0:,}'.format(1493500)
# '1,493,500'
# 만약 정렬을 하고 싶다면 정렬 방향과 길이 뒤에 콤마를 지정해줍니다.
#
# >>> '{0:>20,}'.format(1493500)     # 길이 20, 오른쪽으로 정렬
# '           1,493,500'
# >>> '{0:0>20,}'.format(1493500)    # 길이 20, 오른쪽으로 정렬하고 남는 공간은 0으로 채움
# '000000000001,493,500'