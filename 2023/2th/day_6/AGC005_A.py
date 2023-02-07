from collections import deque
def main():
    X = input()
    stock = deque()
    
    for i in range(len(X)):
        if X[i] == 'S':
            stock.append(X[i])
        else:
            if len(stock) == 0:
                stock.append(X[i])
                continue
            if stock[-1] == 'S':
                stock.pop()
            
            else:
                stock.append(X[i])
                
    print(len(stock))
                

if __name__ == '__main__':
    main()