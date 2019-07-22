# 문자열이 저장된 words.txt 파일이주어집니다(문자열은 한 줄로 저장되어 있습니다).
# words.txt 파일에서 문자 c가 포함된 단어를 각 줄에 출력하는 프로그램을 만드세요.
# 단어를 출력할 때는 등장한 순서대로 출력해야 하며 ,(콤마)와 .(점)은 출력하지 않아야 합니다.
#
# judge_file.py
# ________________
# ________________
# ________________
# ________________
# ________________
#
#
# words.txt
# Fortunately, however, for the reputation of Asteroid B-612,
# a Turkish dictator made a law that his subjects, under pain of death,
# should change to European costume. So in 1920 the astronomer gave his
# demonstration all over again, dressed with impressive style and elegance.
# And this time everybody accepted his report.
# 표준 출력
# dictator
# subjects
# change
# costume
# elegance
# accepted

with open('text.txt', 'r') as file:
    for line in file:
        print(line.strip('\n'))

lines = line.split()

line_l = []
for i in lines:
    words = i.strip(',.''""')
    line_l.append(words)
List = []
for i in line_l:
    for k in i:
        if k == 'c':
            List.append(i)

