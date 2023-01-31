def main():
    from collections import deque
    import heapq
    K = int(input())
    cnt = 1
    que = [1,2,3,4,5,6,7,8,9]
    ans = [1,2,3,4,5,6,7,8,9]
    
    while cnt < K+10: #少し多めに取っておく
        
        num = str(heapq.heappop(que))
        if num[-1] == '0':
            nnum = num + '0'
            heapq.heappush(que,int(nnum))
            cnt += 1
            ans.append(nnum)
            nnum = num + '1'
            heapq.heappush(que,int(nnum))
            ans.append(nnum)
            cnt += 1
            
        elif num[-1] == '9':
            nnum = num + '8'
            heapq.heappush(que,int(nnum))
            ans.append(nnum)
            cnt += 1
            nnum = num + '9'
            heapq.heappush(que,int(nnum))
            ans.append(nnum)
            cnt += 1
            
        else:
            nnum = num + str((int(num[-1]) - 1))
            heapq.heappush(que,int(nnum))
            ans.append(nnum)
            cnt += 1
            nnum = num + num[-1]
            heapq.heappush(que,int(nnum))
            ans.append(nnum)
            cnt += 1
            nnum = num + str(int(num[-1]) + 1)
            heapq.heappush(que,int(nnum))
            ans.append(nnum)
            cnt += 1
            
            
    print(ans[K-1])
            
            
            
            
            
        
        
        
    
    
    
    
    
if __name__ == '__main__':
    main()