N=int(input())
first=['H','D','C','S']
seconds=['A' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , 'T' , 'J' , 'Q' , 'K']
judge=True
use_moji=[]
for i in range(N):
    s=input()
    if s[0] in first:
        if s[1] in seconds:
            if s not in use_moji:
                use_moji.append(s)

            else:
                print('No')
                exit()

        else:
            print('No')
            exit()

    else:
        print('No')
        exit()
 
print('Yes')


                

