import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
 
def main():
    S = input()
    ans = int(S[0])
    for i in range(1,len(S)):
        if i % 2 == 0:
            ans += int(S[i])
            
        else:
            ans -= int(S[i])
    print(ans)
if __name__ == '__main__':
    main()