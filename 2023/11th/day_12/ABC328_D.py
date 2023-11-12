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
    S = list(map(str,input()))
    S = deque(S)
    while True:
        new_que = deque()

        for i in range(len(S)):
            new_que.append(S[i])
            if len(new_que) >= 3:
                if new_que[-3] == "A" and new_que[-2] == "B" and new_que[-1] == "C":
                    new_que.pop()
                    new_que.pop()
                    new_que.pop()
        
        if S == new_que:
            break

        S = new_que

    S = list(S)
    print(''.join(S))


if __name__ == '__main__':
    main()