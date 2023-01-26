
def main():
    N,A,B = map(int,input().split())
    S = input()
    cost = 10**20
    for i in range(N):
        S = S[1:] + S[0]
        tmp = A * ((i+1)%N)
        for j in range(N//2):
            if S[j] != S[N-(j+1)]:
                tmp += B
                
        cost = min(cost,tmp)
         
    print(cost)
                

if __name__ == '__main__':
    main()