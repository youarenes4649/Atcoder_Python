from collections import defaultdict


N = int(input())
S = input()
dic = defaultdict(int)
for s in S:
    dic[s] += 1

n = int((10**N)**0.5)
ans = 0
for i in range(n+1):
    square_num = str(i**2).zfill(N)
    flag = 1
    for k, v in dic.items():
        if square_num.count(k) != v:
            flag = 0
    ans += flag

print(ans)
