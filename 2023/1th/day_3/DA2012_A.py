#https://atcoder.jp/contests/digitalarts2012

def main():
    s = list(map(str,input().split()))
    N = int(input())
    ng = []
    for i in range(N):
        ss = input()
        ng.append(ss)
    ans = []
    for i in range(len(s)):
        check = False
        tmp = list(map(str,s[i]))
        for word in ng:
            if len(s[i]) != len(word):
                continue
            #長さが一緒なら
            for j in range(len(s[i])):
                if word[j] == '*':
                    tmp[j] = '*'
            tmp = ''.join(tmp)
            if tmp == word: 
                check = True
                ans.append(len(word)*'*')
                break
        if check == False:
            ans.append(s[i])
    print(*ans)
            
            
if __name__ == '__main__':
    main()