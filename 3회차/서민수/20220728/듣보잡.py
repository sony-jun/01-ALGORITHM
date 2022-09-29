T = int(input())

for test_case in range(1, T + 1):    
    num = list(input().split())
    lst = []
    arry =[]    
    for i in num:
        if i not in lst:
            lst.append(i)
        if i not in arry:
               	arry.append(i)
print(max(arry))
               