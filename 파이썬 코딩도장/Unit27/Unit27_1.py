#### 파일 사용하기

### 파일에 문자열 쓰기
## 파일에 문자열 쓰기
# * 파일객체 = open(파일이름, 파일모드)
# * 파일객체.write('문자열')
# * 파일객체.close()

file = open('Hello.txt', 'w')   # 파일 생성.꼭 먼저 open으로 열어야 함. 'w'는 쓰기 전용모드
file.write('hi ho silva')       # 파일에 문자열 저장
file.close()                    # 파일 객체 닫기. 꼭 닫아주어야 함

## 파일에서 문자열 읽기
file = open('hello.txt', 'r')   # 읽기 모드로 열기. 파일 객체 반환
s = file.read()
print(s)
file.close()

## 자동으로 파일 객체 닫기
# with open(파일이름, 파일모드) as 파일객체:
#   코드
with open('hello.txt', 'r') as file:
    s = file.read()
    print(s)              # 끝난후 close로 닫지 않아도 됨


### 문자열 여러줄을 파일에 쓰기 읽기

## 반복문으로 문자열 여러줄을 파일에 쓰기
with open('hello.txt', 'w') as file:
    for i in range(3):
        file.write('hi!! world!! {0}\n'.format(i))
# 파일에 문자열 여러줄을 저장할 때 주의할 부분은 개행문자 부분!! 'hi!! world!! {0}\n'와 같이 문자열 끝에 개행문자 \n를
# 지정해주어야 줄바꿈이 가능함. 만약 \n을 붙이지 않으면 문자열이 모두 한 줄로 붙어서 저장되므로 주의해야 합니다.

## 리스트에 들어있는 문자열을 파일에 쓰기
# * 파일객체.writelines(문자열리스트)
lines = ['hi!\n', 'python\n', 'this is a code gym!!\n']

with open('hello.txt', 'w') as file:
    file.writelines(lines)
# writelines 는 리스트에 들어있는 문자열을 파일에 씁니다. 특히 writelines를 사용할 때는 반드시
# 리스트에 문자열 끝에 개행문자 \n을 붙여주어야 합니다. 그렇지 않으면 한줄로 저장됨

## 파일의 내용을 한 줄 씩 리스트로 가져오기
# * 변수 = 파일객체.readlines()
with open('hello.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

## 파일의 내용을 한 줄씩 읽기
# * 변수 = 파일객체.readline()
with open('hello.txt', 'r') as file:
    line = None                 # 변수 line을 None으로 초기화
    while line != '':
        line = file.readline()       # 문자열을 한 줄을 읽어서 변수 line에 저장하기
        print(line.strip('\n'))    # 파일에서 읽어온 문자열에서 \n 삭제하여 출력

# readline으로 파일을 읽을때는 while 반복문을 활용해야 합니다. 왜냐하면 문자열이 얼마나 길지 알수 없으므로
# 특히 변수 line은 while로 반복하기 전에 None으로 초기화 해주어야 함. 만약 번수를 만들지 않고 실행하면
# 없는 변수와 빈 문자열 ''을 비교하게 되므로 에러발생. 또한 line을 None이 아닌 ''으로 초기화 해줄 시
# line != ''은 거짓이 되므로 반복하지 않고 코드가 끝남.

## for 반복문으로 파일의 내용을 줄 단위로 읽기
with open('hello.txt', 'r') as file:
    for line in file:
        print(line.strip('\n'))

# 언패킹( 하나로 묶지 않음)
file = open('hello.txt', 'r')
a, b, c = file      # 갯수가 일치하여야 함
a,b,c


### 파이썬 객체를 파일에 저장하기 가져오기

## 파이썬 객체를 파일에 저장하기
import pickle

name = 'stephen'
age = 17
address = 'golden state'
scores = {'avg score': 30, 'assist':5.2, 'rebound': 5.3, 'field goal': 47.2}

with open('stephen.p', 'wb') as file:   # stephen.p 파일을 바이너리 쓰기 모드(wb)로 열기
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)


# 파일에서 파이썬 객체 읽기
import pickle
with open('stephen.p', 'rb') as file:
    name = pickle.load(file)
    age = pickle.load(file)
    address = pickle.load(file)
    scores = pickle.load(file)    # 네번을 꼭 사용해야함.
    print(name)
    print(scores)

# 참고 | 다른 파일 모드는 없나요?
# 사실 파일 모드는 조합에 따라 여러 종류가 있습니다. 읽기 'r', 쓰기 'w' 이외에 추가
# 'a', 배타적 생성 'x'도 있습니다. 추가 모드는 이미 있는 파일에서 끝에 새로운 내용을 추가할 때
# 사용하고, 배타적 생성 모드는 파일이 이미 있으면 에러(FileExistsError)를 발생시키고 없으면
# 파일을 만듭니다. 'x'는 베타적 생성(exclusive creation)의 x입니다
#
# 또한, 파일의 형식도 함께 지정할 수 있는데, 텍스트 모드 't'와 바이너리 모드 'b'가
# 있습니다. 이 파일 형식과 읽기, 쓰기 모드를 조합한 텍스트 모드 'rt', 'wt'는 파일을
# 텍스트 모드로 엽니다. 특히 텍스트 모드는 생략할 수 있어서 그냥 'r', 'w'도 텍스트 모드입니다.
# 그리고 바이너리 모드 'rb', 'wb' 등은 피클링을 사용하거나 바이너리 데이터를 직접 저장할 때 사용합니다.
#
# 그다음에 '+'가 있는데 파일을 읽기/쓰기 모드로 엽니다. 이 모드는 'r+t', 'w+t', 'r+', 'w+', 'r+b', 'w+b'
# 등으로 조합할 수 있으며 읽기/쓰기 모드인 것은 같지만 파일 처리 방법이 조금씩 다릅니다.


