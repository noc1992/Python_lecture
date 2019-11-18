# 표준 입력으로 문자열이 입력됩니다.
# 입력된 문자열에서 'the'의 개수를 출력하는 프로그램을 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다).
# 단, 모든 문자가 소문자인 'the'만 찾으면 되며 'them', 'there', 'their' 등은 포함하지 않아야 합니다

text = input()
the grown-ups response, this time,was to advise me to lay aside my drawings of boa constrictors, whether from the inside or the outside, and devote myself instead to geography, history, arithmetic, and grammar. That is why, at the, age of six, I gave up what might have been a magnificent career as a painter. I had been disheartened by the failure of my Drawing Number One and my Drawing Number Two. Grown-ups never understand anything by themselves, and it is tiresome for children to be always and forever explaining things to the.

words = text.split()

word_l = []
for i in words:
    word = i.strip(',.')
    word_l.append(word)

print(word_l.count('the'))



# 표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고,
# 각 가격은 ;(세미콜론)으로 구분되어 있습니다. 입력된 가격을 높은 가격순으로 출력하는
# 프로그램을 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다).
# 이때 가격은 길이를 9로 만든 뒤 오른쪽으로 정렬하고 천단위로 ,(콤마)를 넣으세요.
#
# judge_string_alignment.py
# ________________
# ________________
# ________________
# ________________
#
#
# 예
# 입력
# 51900;83000;158000;367500;250000;59200;128500;1304000
# 결과
# 1,304,000
#   367,500
#   250,000
#   158,000
#   128,500
#    83,000
#    59,200
#    51,900

L = list(map(int, input().split(';')))

L.sort(reverse=True)
i=0
for i in L:
    print('{0:>9,}'.format(i))