
def main():
    from itertools import accumulate
    N = int(input())
    S = input()
    white = [0]*(N+1)
    brack = [0]*(N+1)
    for i in range(1,N+1):
        if S[i-1] == '.':
            white[i] = 1
        else:
            brack[i] = 1
            
    white = list(accumulate(white))
    brack = list(accumulate(brack))
    allw = white[-1]
    allb = brack[-1]
    ans = 10**6
    for i in range(N+1):
        w = i - white[i]
        b = N - i - (allb - brack[i])
        
        ans = min(ans,w+b)
    print(ans)
        

if __name__ == '__main__':
    main()