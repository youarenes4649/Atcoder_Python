def main():
    N = int(input())
    S = input()
    kusa1 = [1]*(N)
    kusa2 = [1]*(N)
    for i in range(N-1):
        if S[i] == 'A':
            kusa1[i+1] = kusa1[i] + 1
    for i in range(N-1,0,-1):
        if S[i-1] == 'B':
            kusa2[i-1] = kusa2[i] + 1
            
    ans = [0]*(N)
    for i in range(N):
        ans[i] = max(kusa1[i],kusa2[i])
    
    print(sum(ans))
            
            
            
            
if __name__ == '__main__':
    main()