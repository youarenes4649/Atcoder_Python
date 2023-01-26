
def main():
    from collections import deque
    K = int(input())
    que = [str(i) for i in range(1,10)]
    que_se = [i for i in range(1,10)]
    que = deque(que)
    count = 0
    while True:
        a = que.popleft()
        num = int(a[-1])
        if num != 0:
            aa = a + str(num - 1)
            que.append(aa)
            que_se.append(int(aa))
            count += 1
            
        aa = a + str(num)
        que.append(aa)
        que_se.append(int(aa))
        count += 1
        
        if num != 9:
            aa = a + str(num + 1)
            que.append(aa)
            que_se.append(int(aa))
            count += 1
            

        if count > K:
            que_se.sort()
            print(que_se[K-1])
            exit()
        
    
if __name__ == '__main__':
    main()