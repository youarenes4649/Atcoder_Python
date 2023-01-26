X,Y,Z=map(int,input().split())

if X>0:
    if Y<0:
        print(X)
        exit()
    if X<Y:
        print(X)

    else:
        if Y<Z:
            print(-1)
        
        else:
            if Z<0:
                print(abs(2*Z)+X)

            else:
                print(X)


    

else:
    if Y>0:
        print(abs(X))
        exit()
    if X<Y:
        if Y>Z:
            print(-1)
            exit()
        else:
            if Z>0:
                print(abs(2*Z)+abs(X))

            else:
                print(abs(X))

    else:
        print(abs(X))


        

    

 