
def main():
    from collections import defaultdict
    S = input()
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    check = defaultdict(int)
    for i in range(len(alpha)):
        check[alpha[i]] = i
    ans = 0
    for i in range(1,len(S)):
        ans += 26**(i)+1
        
    for i in range(len(S)):
        s = S[i]
        mae_cnt = check[s]
        ans += mae_cnt*(26**(len(S) - (i+1))) 
        
        
        
    print(ans-(len(S)-2))
        
    
        
        
        
    
        
    
if __name__ == '__main__':
    main()