#### 두점 사이의 거리 구하기

### 두 점 사이의 거리 구하기

## 클래스로 점 구현하기

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point2D(x=30, y=20)
p2 = Point2D(x=50, y=30)

print('p1: {} {}'.format(p1.x, p1.y))
print('p2: {} {}'.format(p2.x, p2.y))


## 피타고라스의 정리로 두 점 거리 구하기
a = p2.x - p1.x
b = p2.y - p1.y

import math

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point2D(x=30, y=20)
p2 = Point2D(x=60, y=50)

a = p2.x - p1.x
b = p2.y - p1.y

c = math.sqrt((a * a) + (b * b))
print(c)