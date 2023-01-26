S=input()
if S[0]=='1':
    print('No')
    exit()


else:     
    retu1=[S[6]]
    retu2=[S[3]]
    retu3=[S[1],S[7]]
    retu4=[S[0],S[4]]
    retu5=[S[2],S[8]]
    retu6=[S[5]]
    retu7=[S[9]]
    retu=[retu1,retu2,retu3,retu4,retu5,retu6,retu7]

    for i in range(len(retu)-1):
        for j in range(i+1,len(retu)):
            
            for k in range(i,j):
                if retu[i].count('0')!=len(retu[i]) and retu[j].count('0')!=len(retu[j]):
                    if retu[k].count('0')==len(retu[k]):
                        print('Yes')
                        exit()

    print('No')