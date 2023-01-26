
def main():
    def func(N):
        if (N) % 2 == 0:
            if (N//2)%2 == 0: 
                fa = N
            else:
                fa = 1 ^ N
        else:
            if (N//2)%2 == 0: 
                fa = (N-1) ^ (N)
            else:
                fa = 1 ^ (N-1) ^ (N)
            
        return fa      
    A,B = map(int,input().split())
    print(func(A-1) ^ func(B))
         
if __name__ == '__main__':
    main()