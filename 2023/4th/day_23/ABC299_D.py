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
    cnt = 0
    ok = N
    ng = 0
    check = [-1] * (N + 1)
    while ok - ng > 1:
        mid = (ok + ng) // 2
        print('?',mid,flush = True)
        ans = input()
        if ans == '0':
            ng = mid
        else:
            ok = mid
        check[mid] = int(ans)

    print('!',ok-1,flush=True)
        
if __name__ == '__main__':
    main()