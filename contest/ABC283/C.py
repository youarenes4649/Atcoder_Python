S = list(map(str,input()))
from collections import deque
S_que = deque(S)
ans = []
i = 0

ans = len(S)
while i <len(S) :
    if S[i] == '0' and S[i+1] =='0':
        ans -= 1
        i += 2
        continue
    
    i+=1
print(ans)
    