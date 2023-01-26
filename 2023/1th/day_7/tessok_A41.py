

def main():
    N = int(input())
    S = input()
    ans = ['W']*(N)
    i = 0
    while i < N-3:
        if S[i] == 'R':
            
            for j in range(3):
                ans[i+j] = 'R'
        else:
            for j in range(3):
                ans[i+j] = 'B'
                
        i += 1
    print(ans)
                
    
        
if __name__ == '__main__':
    main()