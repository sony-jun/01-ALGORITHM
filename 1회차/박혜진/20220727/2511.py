a_li =[] 
b_li =[] 

a_li=list(map(int,input().split())) 
b_li=list(map(int,input().split()))

a = 0 
b = 0 
count = 0 
for i in range(10): 
    if a_li[i] > b_li[i]: 
        a+=3 
    elif b_li[i] > a_li[i]: 
        b+=3 
    elif b_li[i] == a_li[i]: 
        a+=1 
        b+=1 
        if b_li[i-1] != a_li[i-1]: 
            count = i-1 
print(a, b)

if a > b: 
    print('A') 
elif a == b: 
    if b_li[count] > a_li[count]: 
        print("B") 
    elif b_li[count] < a_li[count]:
        print("A") 
    else: 
        print("D") 
elif b > a: 
    print('B')