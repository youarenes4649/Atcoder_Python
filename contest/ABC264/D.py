S='atcoder'
T=input()
#転倒数　sの隣接項の入れ替えによりsを昇順にするための入れ替え最小回数
#バブルソートでマンに合う
#自分より小さい数が右に何個あるかで転倒数になる
from collections import defaultdict
cnt=defaultdict(int)
S_cnt=[0,1,2,3,4,5,6]
T_cnt=[]
for i ,c in enumerate(S):
    cnt[c]=i
for i in range(7):
    T_cnt.append(cnt[T[i]])

ans=0
for i in range(7):
    t=T_cnt[i]
    for j in range(i+1,7):
        if T_cnt[j]<t:
            ans+=1

print(ans)






