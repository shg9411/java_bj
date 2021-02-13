import io
import os
import sys
input = sys.stdin.readline
#input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def solve():
    R, C = map(int, input().split())
    parent = [i for i in range(R*C)]
    cost = []
    for i in range(R):
        for j, v in enumerate(map(int, input().split()), start=i*C):
            cost.append((v, j, j+1))
    for i in range(R-1):
        for j, v in enumerate(map(int, input().split()), start=i*C):
            cost.append((v, j, j+C))
    cost.sort()

    def find(x):
        if parent[x] == x:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        x, y = find(x), find(y)
        parent[y] = x

    cnt = res = 0
    total = R*C-1
    for a, b, c in cost:
        if find(b) == find(c):
            continue
        cnt += 1
        res += a
        union(b, c)
        if cnt == total:
            return res


if __name__ == '__main__':
    res = []
    for _ in range(int(input())):
        res.append(solve())
    sys.stdout.write('\n'.join(map(str, res)))
