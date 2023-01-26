S=[]
cnt=0
start=0
for i in range(10):
    s=list(map(str,input()))
    if "#" in s :
        cnt+=1
        if start==0:
            start=i+1
    S.append(s)
cnt2=0
start2=0
for s in range(len(S[start-1])):
    if '#'==S[start-1][s]:
        cnt2+=1
        if start2==0:
            start2=s+1

print(start,start+cnt-1)
print(start2,start2+cnt2-1)




