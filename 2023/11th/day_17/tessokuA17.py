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
    A = li()
    B = li()

    dp = [inf] * (N)
    dp[0] = 0 #部屋１
    dp[1] = A[0] #部屋２

    for i in range(2,N):
        dp[i] = min(dp[i], dp[i-1] + A[i-1], dp[i-2]+B[i-2])

    now = N-1
    ans = [now]
    while now > 0:
        if dp[now] == dp[now-1] + A[now-1]:
            ans.append(now-1)
            now = now-1
        else:
            ans.append(now-2)
            now -= 2

    for i in range(len(ans)):
        ans[i] += 1

    print(len(ans))
    print(*ans[::-1])


if __name__ == '__main__':
    main()