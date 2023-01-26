S = list(map(str,input()))
from collections import defaultdict,deque
c2n = defaultdict(int)
ch = 'abcdefghijklmnoprstuvwxyz'
for i in range(len(ch)):
    c2n[ch[i]] = i
ball = [0]*(len(ch)) #ball is flag to indicate
right = 0
left = 0
S_que = deque()
for i in range(len(S)):
    if S[i] == '(':
        S_que.append('(')
        continue
    
    if S[i] == ')':
      
        while S_que[-1] != '(':
            num = S_que.pop()
            if num != ')':
                ball[c2n[num]] -= 1
        S_que.pop()
        
        continue
    else:
        if ball[c2n[S[i]]] != 0:
            print('No')
            exit()
        S_que.append(S[i])
        
        ball[c2n[S[i]]] += 1
        
            
print('Yes')
        
        