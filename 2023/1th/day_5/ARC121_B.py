
def main():
    from collections import defaultdict
    import bisect
    color = defaultdict(list)
    N = int(input())
    for _ in range(2*N):
        a,c = input().split()
        a = int(a)
        color[c].append(a)
        
    color['R'].sort()
    color['G'].sort()
    color['B'].sort()
    if len(color['R'])%2 == 0 and len(color['G'])%2 == 0 and len(color['B'])%2 == 0:
        print(0)
    else:# ぐ　き　き　の時
        if len(color['R'])%2 == 0 :
            kk = 10**20 #き　き　からとる
            for i in range(len(color['G'])):
                idx = bisect.bisect_right(color['B'],color['G'][i])
                kk = min(kk,abs(color['B'][idx]-color['G'][i]),abs(color['B'][idx-1]-color['G'][i]))
            
            kk2 = 10**20#　ぐ　き　からとる
            kk22 = 10**20
            for i in range(len(color['R'])):
                idx = bisect.bisect_right(color['B'],color['R'][i])
                kk2 = min(kk2,abs(color['B'][idx]-color['R'][i]),abs(color['B'][idx-1]-color['R'][i]))
                idx2 = bisect.bisect_right(color['G'],color['R'][i])
                kk22 = min(kk22,abs(color['G'][idx2]-color['R'][i]),abs(color['G'][idx2-1]-color['R'][i]))
            
            print(min(kk,kk2+kk22))
            
        if len(color['G'])%2 == 0 :
            kk = 10**20 #き　き　からとる
            for i in range(len(color['R'])):
                idx = bisect.bisect_right(color['B'],color['R'][i])
                kk = min(kk,abs(color['B'][idx]-color['R'][i]),abs(color['B'][idx-1]-color['R'][i]))
            
            kk2 = 10**20#　ぐ　き　からとる
            kk22 = 10**20
            for i in range(len(color['G'])):
                idx = bisect.bisect_right(color['B'],color['G'][i])
                kk2 = min(kk2,abs(color['B'][idx]-color['G'][i]),abs(color['B'][idx-1]-color['G'][i]))
                idx2 = bisect.bisect_right(color['R'],color['G'][i])
                kk22 = min(kk22,abs(color['R'][idx2]-color['G'][i]),abs(color['R'][idx2-1]-color['G'][i]))
            
            print(min(kk,kk2+kk22))
            
        if len(color['B'])%2 == 0 :
            kk = 10**20 #き　き　からとる
            for i in range(len(color['R'])):
                idx = bisect.bisect_right(color['G'],color['R'][i])
                kk = min(kk,abs(color['G'][idx]-color['R'][i]),abs(color['G'][idx-1]-color['R'][i]))
            
            kk2 = 10**20#　ぐ　き　からとる
            kk22 = 10**20
            for i in range(len(color['B'])):
                idx = bisect.bisect_right(color['G'],color['B'][i])
                kk2 = min(kk2,abs(color['G'][idx]-color['B'][i]),abs(color['G'][idx-1]-color['B'][i]))
                idx2 = bisect.bisect_right(color['R'],color['B'][i])
                kk22 = min(kk22,abs(color['R'][idx2]-color['B'][i]),abs(color['R'][idx2-1]-color['B'][i]))
            
            print(min(kk,kk2+kk22))                       
                
                
        
        
        
        
        
if __name__ == '__main__':
    main()