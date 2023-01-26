
def main():
    N = int(input())
    card = []
    for _ in range(N):
        a,b = map(int,input().split())
        card.append([a,b])
    ans = 0
    for i in range(4):
        tmp = 0
        if i == 0:
            for j in range(N):
                a,b = card[j]
                if a + b > 0:
                    tmp += a+b
            ans = max(ans,tmp)
        if i == 1:
            for j in range(N):
                a,b = card[j]
                if a - b > 0:
                    tmp += a-b
            ans = max(ans,tmp)
        if i == 2:
            for j in range(N):
                a,b = card[j]
                if -a + b > 0:
                    tmp += -a+b
            ans = max(ans,tmp)
        if i == 4:
            for j in range(N):
                a,b = card[j]
                if -a - b > 0:
                    tmp += -(a+b)
            ans = max(ans,tmp)
            
    print(ans)
                
if __name__ == '__main__':
    main()