
def main():
    N = int(input())
    A = list(map(str,input()))
    B = list(map(str,input()))
    mod = 998244353
    
    #一番数字が離れている時が最小？Aを最小にしてBを最大にする
    for i in range(N):
        if A[i] > B[i]:
            A[i],B[i] = B[i],A[i]
            
    A = int(''.join(A))
    B = int(''.join(B))
    print(A*B%mod)
    
        
if __name__ == '__main__':
    main()