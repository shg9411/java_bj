import math
n = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    t = math.gcd(a, b)
    n.append((a//t, b//t))
x, y = n[0]
for a, b in n[1:]:
    x = math.gcd(a, x)
    y = b*y//math.gcd(b, y)
#t = math.gcd(x, y)
#print(x//t, y//t)
print(x,y)
