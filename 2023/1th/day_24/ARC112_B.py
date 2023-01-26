
def main():
    B,C = map(int,input().split())
    if B > 0:
        if C >= 2*B:
            cost = C - B * 2
            if cost > B:
                ans = B * 2 + 1 + B
                
                ans += 2*(cost - B - 1) + 1
                
                
            else:
                ans = B * 2 + 1+ cost
            print(ans)
         
        else:
            print(2 * (C-1) + 1)
            
    if B == 0:
        print(C)
        

    
if __name__ == '__main__':
    main()