result_list = []
while True:
    A, B = map(int, input().split())
    if A==0 and B==0:
        for i in result_list:
            print(i)
        break
    
    result = A + B
    result_list.append(result)
    