N=int(input())
P=list(map(int,input().split()))
def count_inversion(sequence):
    count = 0
    for i in range(1,len(sequence),1):
        for j in range(i,len(sequence),1):
            if sequence[i-1] > sequence[j]:
                count += 1
    return count

use=[]
import bisect
for i in range(N-1,0,-1):
    cnt=0
    if P[i-1]>P[i]:
        cnt+=1

    use.append(P[i])
    ans=[]
    
    if cnt>0:
        anss=P[:i-1]
        use.sort()
        idx=bisect.bisect_left(use,P[i-1])
  
        ans.append(use[idx-1])
        del use[idx-1]
        use.append(P[i-1])
        use.sort()
        ans.extend(use[::-1])
        anss.extend(ans)
        print(*anss)
        exit()




