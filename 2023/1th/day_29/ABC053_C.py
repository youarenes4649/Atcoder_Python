
def main():
    x = int(input())
    if x % 11 == 0:
        print(2*x//11)
        exit()
    ans = 2*x//11 #奇数回なら５　偶数回なら6
    
    total = 6 * (ans//2) + 5 * (ans - ans//2)
    if ans % 2 == 0:
        #次は5
        if x - total <= 5 :
            ans += 1
            
        else:
            ans += 2
            
    else:
        #次は6
        if x - total <= 6 :
            ans += 1
            
        else:
            ans += 2
            
    print(ans)
if __name__ == '__main__':
    main()