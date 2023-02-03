
def main():
    N = int(input())
    S = list(map(str,input()))
    char_loc = []
    
    # 辞書順最小かつidx 番号が後ろから
    for i,s in enumerate(S):
        char_loc.append((s,i))
    char_loc.sort(key = lambda x: [x[0],-x[1]])
    
    #できるだけ辞書順最小の文字を早めに交換することが最適
    now_point = 0
    end = N #交換候補の文字
    for l in range(N):
        while (l >= char_loc[now_point][1] or end < char_loc[now_point][1]) and now_point < N :
            now_point += 1
        if now_point >= N:
            break
        if S[l] > S[now_point] and l < now_point:
            S[l],S[now_point] = S[now_point],S[l]
            end = S[now_point][1]
            
    
        
    print(''.join(S))
        
        
        
        
            
        
            
if __name__ == '__main__':
    main()