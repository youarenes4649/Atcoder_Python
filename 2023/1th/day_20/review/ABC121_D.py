
def main():
    A,B = map(int,input().split())
    
    if A%2 == 0 and B%2 == 0:
        cnt = (B-A)//2
        print(B ^ (cnt%2))
    elif A%2 == 0 and B%2 == 1:
        cnt = (B+1) - A
        cnt //= 2
        print(cnt%2)
    elif A%2 == 1 and B%2 == 0:
        cnt = (B-1) - A
        cnt //= 2
        print(A ^ (cnt%2) ^ B)
        
    else:
        cnt = B - A 
        cnt //= 2
        print(A ^ (cnt%2))
        
        
        
    
    
    
    
    
    
if __name__ == '__main__':
    main()