V,A,B,C=map(int,input().split())


while V>0:
    if V-A>=0:
        V-=A
        
        if  V-B>=0:
            V-=B

            if V-C<0:
                print('T')
                exit()

            else:
                V-=C
                continue

        else:
            print('M')
            exit()

        

    else:
        print('F')
        exit()

print('F')
    
