# 심사문제 8
korean, english, mathematics, science = map(int, input().split(','))
print(bool(korean >= 90 and english > 80 and mathematics >85  and science >= 80))

# 심사문제 9
s = '''\'Python\' is a "programming language"
that lets you work quickly
and
integrate systems more effectively.'''

# 심사문제 10
a = int(input())
print(tuple(range(-10, 10, a)))

#심사문제 11-8
x = input().split()
print(tuple(x[:len(x) - 5])

# 심사문제 11-9
a = input()
b = input()
c = a[1:len(a):2]
d = b[0:len(b):2]
print(c + d)

# 심사문제 12
a = input().split()
b = list(map(float, input().split()))
print(dict(zip(a[:], b[:])))