S=list(map(str,input()))
judge_upper=0
judge_lower=0
for s in S:
    if s.isupper()==True:
        judge_upper+=1

for s in S:
    if s.islower()==True:
        judge_lower+=1


lens=len(S)
set_s=len(set(S))

if judge_lower!=0 and judge_upper!=0 and lens==set_s:
    print('Yes')

else:
    print('No')

        
    