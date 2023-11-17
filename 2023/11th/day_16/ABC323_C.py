import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
from collections import deque
def main():
    K = ii()
    que = deque([])
    for i in range(1,10):
        que.append(i)
    cnt = 0
    while cnt < K:
        now = que.popleft()
        cnt += 1

        now = str(now)
        if now[-1] == "0":
            continue

        
        for i in range(int(now[-1])):
            que.append(int(now + str(i)))

    
    print(now)

if __name__ == '__main__':
    main()