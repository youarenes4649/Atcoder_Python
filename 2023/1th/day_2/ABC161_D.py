
def main():
    K = int(input())
    from collections import deque
    
    li = [str(i) for i in range(1,10)]
    st_li = li[:]
    que = deque(li)
    count = 0
    n = 10**10
    
    for i in range(1,n):
        a = que.popleft()
        num = int(a[-1])
        
        if num != 0:
            aa = a + str(num-1)
            que.append(aa)
            st_li.append(aa)
            count += 1
            
        aa = a + str(num)
        que.append(aa)
        st_li.append(aa)
        count += 1
        if num != 9:
            aa = a + str(num+1)
            que.append(aa)
            st_li.append(aa)
            count += 1
        if count > K:
            print(st_li[K-1])
            exit()
        
    
if __name__ == '__main__':
    main()