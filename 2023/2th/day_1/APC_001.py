
def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    biggerA = 0
    biggerB = 0
    for i in range(N):
        if A[i] - B[i] > 0:
            biggerA += A[i] - B[i]
        if B[i] - A[i] > 0:
            biggerB += (B[i] - A[i] + 1) //2
            
    if biggerA > biggerB:
        print('No')
        
    else:
        print('Yes')
if __name__ == '__main__':
    main()    
