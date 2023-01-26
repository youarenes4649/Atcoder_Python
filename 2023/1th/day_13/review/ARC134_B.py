def zaatsu(a:list) -> (dict, dict):
    """
    配列aの要素番号を与えると位置が返ってくる
    配列の位置番号を与えると要素が返ってくる
    """
    s = sorted(list(set(a)))
    press = {x:i+1 for i,x in enumerate(s)}
    expand = {i+1:x for i,x in enumerate(s)}
    return press, expand

def main():
    N = int(input())
    S = list(map(str,input()))
    p,e = zaatsu(S)#p: 文字を入れたら辞書順を教えてくれる
    pos = []
    for i,c in enumerate(S):
        pos.append((c,i))
    pos.sort(key=lambda x : [x[0],-x[1]] )#これで辞書最小順で後ろにある順になった
    ans = S
    now = 0
    r = N
    for l in range(N):
        sl = S[l]
        while  now < N and (i >= pos[now][1] or r < pos[now][1]):#辞書順で小さくない限り
            now += 1
        if now >= N:
            break
        if sl > pos[now][0]:
            j = pos[now][1]
            S[i],S[j] = S[j],S[i]
            r = j
            now += 1
            

    print(''.join(S))
        
        
        
    
if __name__ == '__main__':
    main()