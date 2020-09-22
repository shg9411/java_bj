import sys

d, p, q = map(int, input().split())
if d % p == 0 or d % q == 0:
    print(d)
    exit()
if p < q:
    p, q = q, p

r = sys.maxsize
for i in range(d//p+2):
    tq = (d-p*i)//q
    for j in range(max(0, tq-2), tq+2):
        if (tr := p*i+q*j) < d:
            continue
        r = min(r, tr)
print(r)
