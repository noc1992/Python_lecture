# unit 23

c, r = list(map(int, input().split()))

a = []
for i in range(c):
    line = []
    for k in range(r):
        line.append(0)
    a.append(line)

print(a)

a = [[0 for k in range(r)] for i in range(c)]

b = [[0] * 3 for i in range(7)]
print(b)

for i in range(3):
    line= []

from pprint import pprint

pprint(mine, indent=4, width=20)