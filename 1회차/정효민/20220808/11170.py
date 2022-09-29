


t = int(input())

for _ in range(1 , t + 1):
    result = 0
    x , y = input().split()
    a  = int(x)
    b = int(y)
    for all in range(a, b + 1 ):
        cnt = str(all).count('0')
        if cnt > 0:
            result = result + cnt
    
    print(result)
    
