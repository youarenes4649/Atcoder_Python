
def main():
    from collections import deque
    N = int(input())
    S = input()
    stock = []
    for i in range(N):
        if S[i] == 'R':
            cnt_a = 1
            #連続でAが何回続く？
            while i-cnt_a >= 0 and S[i-cnt_a] == 'A':
                cnt_a += 1
                
            cnt_c = 1
            #連続でCが何回続�
            while i + cnt_c < N and S[i+cnt_c] == 'C':
                cnt_c += 1
            num = min(cnt_a-1, cnt_c-1)
            if num >= 1:
                stock.append(num)
            
    
    ans = 0
    count = 1
    
    stock.sort()
    stock = deque(stock)
    while len(stock) > 0:
        if count%2 == 0:
            ans += 1
            stock.popleft()
        else:
            now = stock.pop()
            ans +=1
            if now > 3:
                stock.append(now-1)
            elif now == 2:
                stock.appendleft(1)
            else:
                continue
      
        count += 1
    print(ans)
        
            
                
            
            
            
                 
if __name__ == '__main__':
    main()