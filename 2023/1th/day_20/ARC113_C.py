def main():
    import bisect
    from collections import deque,defaultdict
    S = input()
    stock = deque([])
    dic = defaultdict(list)
    len_s = len(S)
    for i in range(len_s-1):
        if S[i] == S[i+1]:
            stock.append([S[i],i+2])
        dic[S[i]].append(i+1)
    ans = 0
    
    for i in range(len(stock)-1):
        if stock[i][0] != stock[i+1][0]:
            
            dic[stock[i][0]].sort()
            a = stock[i][1]
            b = stock[i+1][1]
            idxa = bisect.bisect_right(dic[stock[i][0]],a)
            idxb = bisect.bisect_right(dic[stock[i][0]],b)
            ans -= (idxb-idxa)
            ans += len_s - stock[i][1]
            
        else:
            dic[stock[i][0]].sort()
            a = stock[i][1]
            b = stock[i+1][1]
            idxa = bisect.bisect_right(dic[stock[i][0]],a)
            idxb = bisect.bisect_right(dic[stock[i][0]],b)
            ans -= (idxb-idxa)
            ans += (stock[i+1][1]-1) - (stock[i][1]+1)
    if len(stock) != 0:
        dic[stock[-1][0]].sort()
        a = stock[-1][1]
        b = len_s
        idxa = bisect.bisect_right(dic[stock[-1][0]],a)
        idxb = bisect.bisect_right(dic[stock[-1][0]],b)
    
        ans -= (idxb-idxa)
        ans += len_s - stock[-1][1]  

            
    print(ans)

        
if __name__ == '__main__':
    main()