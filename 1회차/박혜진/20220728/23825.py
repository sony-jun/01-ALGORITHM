s, a = map(int, input().split())

if s // 2 == a // 2 :
    print(s // 2)
    
else :
    if s // 2 > a // 2 :
        print(a // 2)
    else :
        print(s // 2)