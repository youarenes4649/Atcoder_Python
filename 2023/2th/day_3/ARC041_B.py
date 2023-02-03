
def main():
    N,M = map(int,input().split())
    B = [list(map(int,input())) for i in range(N)]

    A = [[0] * M for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if i - 1  < 0 or i + 1 >=N or j - 1 < 0 or j + 1 >= M:
                continue
            
            ameba =  min(int(B[i-1][j]),int(B[i+1][j]),int(B[i][j-1]),int(B[i][j+1]))
            if ameba >= 1:
                B[i-1][j] -= ameba
                B[i][j-1] -= ameba
                B[i][j+1] -= ameba
                B[i+1][j] -= ameba
                A[i][j] += ameba
                

    for i in range(N):
        tmp = ''
        for j in range(M):
            tmp += str(A[i][j])
        
        print(tmp)
  
                
 
if __name__ == '__main__':
    main()