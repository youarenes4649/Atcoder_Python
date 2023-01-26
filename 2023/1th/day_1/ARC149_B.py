
def main():
    import bisect
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    arr = []
    for a,b in zip(A,B):
        arr.append([a,b])
        
    arr.sort()
    LISB = [arr[0][1]]
    for i in range(len(arr)):
        if LISB[-1] < arr[i][1]:
            LISB.append(arr[i][1])
        else:
            LISB[bisect.bisect_left(LISB,arr[i][1])] = arr[i][1]
    
    print(N + len(LISB))
        
        
    
    
if __name__ == '__main__':
    main()

