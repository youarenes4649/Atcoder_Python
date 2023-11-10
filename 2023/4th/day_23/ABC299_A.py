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
    N = ii()
    S = input()
    left = -1
    right = -1
    ast = -1
    for i in range(N):
        if S[i] == '|':
            if left == -1:
                left = i
                continue
            if right == -1:
                right = i
                continue
        if S[i] == '*':
            ast = i
    if left < ast < right:
        print('in')
    else:
        print('out')
if __name__ == '__main__':
    main()