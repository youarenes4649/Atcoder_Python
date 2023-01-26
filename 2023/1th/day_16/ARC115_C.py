
def main():
    N = int(input())
    A = [0]*(N)
    A[0] = 1
    for i in range(1,N+1):
        for j in range(i,N+1,i):
            print(j)
            if j - 1  > N :
                break      
            if j == i:
                continue
            
            A[j-1] = A[i-1] + 1
            
    print(*A)
            
if __name__ == '__main__':
    main()