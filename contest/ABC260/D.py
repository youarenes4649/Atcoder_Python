#D

import bisect

N, K = list(map(int, input().split(" ")))
P = list(map(int, input().split(" ")))

top = []
#最終的に一番上にあるcardのeatenを参照すればいい
cardabove = [-1]*(N+1)#これが俺には思いつかなかった
totalcardnum = [-1]*(N+1)
eaten = [-1]*(N+1)

for a in range(N):
    num = P[a]
    idx = bisect.bisect_left(top, num)
    if idx == len(top):
        top.append(num)
        totalcardnum[num] = 1
    else:
        cardabove[top[idx]] = num
        totalcardnum[num] = totalcardnum[top[idx]]+1
        top[idx] = num
    if totalcardnum[num] == K:
        eaten[num] = a+1
        del top[idx]
        
for i in reversed(P):#必ず小さいカードが上にくるからこれでもok
    if cardabove[i] != -1:
        eaten[i] = eaten[cardabove[i]]
        
for i in range(1,N+1):
    print(eaten[i])


