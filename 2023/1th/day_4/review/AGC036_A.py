
def main():
    S  = int(input())
    x1,y1 = 0,0
    y3 = 1
    x2 = 10**9 + 1
    y2 = S//x2
    x3 = S%x2
    print(x1,y1,x2,y2,x3,y3)
    
    
if __name__ == '__main__':
    main()