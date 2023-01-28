
def main():
    S = input()
    T = input()
    
    #一度マッチしなくなったら全てnot
    
    start = S[-len(T):]
    check = False
    mojiretu = [True]*len(T)
    for i in range(len(T)):
        if start[i] != T[i] and (start[i] != "?"  and T[i] != '?'):
            check = True
            mojiretu[i] = False
            
            
   
    cnt = mojiretu.count(False)
        
 
    if check == False:
        print('Yes')
        for i in range(len(T)):
            moji = S[i]
            if moji != T[i] and T[i] != '?' and moji != '?':
                for j in range(len(T) - i):
                    print('No')
                    
                exit()
                    
            else:
                print('Yes')
                
    else:#最初からnoの時
        print('No')
        for i in range(len(T)):
            moji = S[i]
            if mojiretu[i]:
                if moji =='?' or moji == T[i] or T[i] == '?':
                    if cnt <=0:
                        print('Yes')
                    else:
                        
                        print('No')
                    
                else:
                    for j in range(len(T)-i):
                        print('No')
                        
                    exit()
                    
            else:

                if moji == '?' or moji == T[i] :
                    cnt -= 1
                    if cnt <= 0:
                        print('Yes')
                    else:
                        print('No')
                else:
                    for j in range(len(T)-i):
                        print('No')
                        
                    exit()
       
if __name__ == '__main__':
    main()