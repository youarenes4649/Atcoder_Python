def main():
    X,Y = map(int,input().split())
    k = 0
    ans = [(X,Y)]
    while X >1 or Y > 1:
        if X > Y:
            X -= Y
        else:
            Y -= X
            
        ans.append((X,Y))
        k += 1

    
    if k == 0:
        print(k)
        exit()
    else:
        print(k)
        ans.reverse()
        for i in range(1,k+1):
            print(*ans[i])
            
        
if __name__ == '__main__':
     main()