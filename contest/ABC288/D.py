
def main():
    from itertools import accumulate
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    A_sum = [0] + list(accumulate(A))
    a_sub = []
    for i in range(N-1):
        a_sub.append(A[i] - A[i+1])
    a_sub.reverse()
    A_sub_sum = [0] + list(accumulate(a_sub))
    Q = int(input())
    for _ in range(Q):
        l,r = map(int,input().split())
        a_sum = A_sum[r]-A_sum[l-1]
        print(a_sum)
        A_tmp = A[l-1:r]
        sub_tmp = sum(a_sub[r-K+2:r+1])
        print(sub_tmp)
        a_sum += K * (-A_tmp[0])
        a_sum += K * (-A_tmp[-1])
        a_sum += -K*sub_tmp
        print(a_sum)
        if a_sum == 0:
            print('Yes')
        else:
            print('No')
            
      
if __name__ == '__main__':
    main()