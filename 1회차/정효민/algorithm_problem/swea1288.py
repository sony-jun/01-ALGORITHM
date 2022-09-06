import sys



sys.stdin = open('s1288.txt')
t = int(input())
for test_case in range(1 , t + 1):
    numbe = [0] * 10
    

    N = int(input())
    result = []
    i = 1
    
    while 0 in numbe:
        numi = str(N * i)
        for j in numi:
            if int(j) not in numbe:
                numbe[int(j)] = int(j)
            
            i = i + 1
    print(i, '12')
        