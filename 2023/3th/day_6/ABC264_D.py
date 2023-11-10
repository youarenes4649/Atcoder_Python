import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
from collections import defaultdict
def main():
    S = list(map(str,input()))
    L = len(S)
    change = defaultdict(str)
    alpabet = 'abcdefg'
    now = 'atcoder'
    for i in range(L):
        change[now[i]] = alpabet[i]
    for i in range(L):
        S[i] = change[S[i]]
        
    ans = 0
    for i in range(L - 1):
        for j in range(L - 1 - i): # 一番右に最も大きい文字が来るようになるから終端数を１減らす
            if S[j] > S[j + 1]:
                S[j],S[j+1] = S[j+1],S[j]
                ans += 1
    print(ans)
if __name__ == '__main__':
    main()