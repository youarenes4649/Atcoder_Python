
def main():
    from collections import deque,defaultdict
    S = list(map(str,input()))
    ans = deque()
    cnt = defaultdict(int)
    ans.append([])
    for i in range(len(S)):
        if S[i] == '(':
            ans.append([])
        elif S[i] == ')':
            arr = ans.pop()  
            for j in arr:
                cnt[j] -= 1
            
        else: 
            if cnt[S[i]] == 0:
                cnt[S[i]] = 1
            else:
                print('No')
                exit() 
            ans[-1].append(S[i])
                
    print('Yes')
if __name__ == '__main__':
    main()