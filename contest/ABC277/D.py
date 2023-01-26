n, m = map(int, input().split())
a = list(sorted(map(int, input().split())))

a += a#2回見てあげればいい
a.append(m)

ans = 0
cnt = a[0]
for i in range(2 * n):#nでおわるのか
    if a[i + 1] == a[i] or a[i + 1] == (a[i] + 1) % m:#問題文に沿った行動ができるのであれば
        cnt += a[i + 1]
    else:
        ans = max(ans, cnt)
        cnt = a[i + 1]

print(max(0, sum(a[:n]) - ans))
