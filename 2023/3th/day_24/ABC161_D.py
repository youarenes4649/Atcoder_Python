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
K = ii()
ans = []
que = deque([])
for i in range(1,10):
    que.append(i)
    
while len(ans) <= K :
    now = que.popleft()
    ans.append(now)
    next_num = int(str(now)[-1])
    if next_num != 0:
        que.append(10 * now + next_num - 1)
    que.append(10 * now + next_num)
    if next_num != 9:
        que.append(10 * now + next_num + 1)
ans.sort()
print(ans[K-1])
    
