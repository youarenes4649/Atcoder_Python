import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
from collections import defaultdict
def main():
    S = input()
    # abcにできればいい
    cnt = [0] * 3
    for s in S:
        if s == 'a':
            cnt[0] += 1
        if s == 'b':
            cnt[1] += 1
        if s == 'c':
            cnt[2] += 1
            
    min_c = min(cnt)
    for i in range(3):
        cnt[i] -= min_c
    if max(cnt) <= 1:
        print('YES')
    else:
        print('NO')
if __name__ == '__main__':
    main()