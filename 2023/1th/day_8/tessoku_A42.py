
def main():
    N,K = map(int,input().split())
    student = []
    for _ in range(N):
        a,b = map(int,input().split())
        student.append([a,b])
    
    check = [[False]*N for _ in range(N)]
    for i in range(N):
        check[i][i] = True
        
    ans = 0
    for a in range(1,101):
        for b in range(1,101):
            tmp_ans = 0
            for n in range(N):
                if a <= student[n][0] <=a+K and b <= student[n][1] <= b+K:
                    tmp_ans += 1
                    
            ans = max(ans,tmp_ans)
            
    print(ans)
                    
if __name__ == '__main__':
    main()