
def main():
    A,B,K = map(int,input().split())
    
    if K >= A:
        K -= A
        A = 0
        
    else:
        A -= K
        print(A,B)
        exit()
        
    if K >= B:
        print(0,0)
        exit()
        
    else:
        print(A,B-K)
        
    
if __name__ == '__main__':
    main()