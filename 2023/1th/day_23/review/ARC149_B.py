
def main():
    import bisect
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    LIS = []
    for i in range(N):
        LIS.append((A[i],B[i]))
        
    LIS.sort()
    B = [LIS[i][1] for i in range(N)]
    
    lis_b = [B[0]]
    for i in range(N):
        if lis_b[-1] < B[i]:
            lis_b.append(B[i])
        else:
            lis_b[bisect.bisect_left(lis_b,B[i])] = B[i]
            
    print(N + len(lis_b))
    
if __name__ == '__main__':
    main()