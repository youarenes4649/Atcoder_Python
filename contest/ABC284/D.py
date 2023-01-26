def factorize(n):
    fct = []  # prime factor
    b, e = 2, 0  # base, exponent
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e = e + 1
        if e > 0:
            fct.append(b)
            return fct
        b, e = b + 1, 0
    if n > 1:
        fct.append(n)
    return fct

def main():
    print(factorize(2023))
    T = int(input())
    for i in range(T):
        N = int(input())
        #pを探す
        pq = factorize(N)[0]
        
        if N % (pq**2) == 0:
            p = pq
            q = N // (pq**2)
           
            
        else:
            p = (N // pq)**0.5
            q = pq
            
        print(int(p), q)
    
if __name__ == '__main__':
    main()