
def main():
    S = list(map(str,input()))
    from collections import defaultdict
    cnt = defaultdict(int)
    stock = [[]]
    for i in range(len(S)):
        if S[i] == '(':
            stock.append([])
            
        elif S[i] == ')':
            for s in stock[-1]:
                cnt[s] -= 1 
            stock.pop()
            
        else:
            stock[-1].append(S[i])
            if cnt[S[i]] != 0:
                print('No')
                exit()
            cnt[S[i]] += 1
            
            
    print('Yes')
if __name__ == '__main__':
    main()