
def main():
    from collections import deque
    K,T = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort(reverse=True)
    Amax = A[0]
    A = A[1:]
    if Amax > sum(A):
        print(Amax-sum(A)-1)
    else:
        print(0)
        
if __name__ == '__main__':
    main()