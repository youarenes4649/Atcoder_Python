
def main():
    import bisect
    N,C,K = map(int,input().split())
    T = []
    for _ in range(N):
        t = int(input())
        T.append(t)
    T.sort()
    
    bus = 0
    i = 0
    while i < N:
        idx = bisect.bisect_left(T,T[i] + K)
        if idx - i >= C:
            i += C
             
        else:
            i += idx - i
        
        bus += 1
        
        
    print(bus)
            
                    
        
if __name__ == '__main__':
    main()