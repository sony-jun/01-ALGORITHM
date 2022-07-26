N = input()
number = list(map(int,input().split()))
total = []
a=0
b=a + 2
while b < len(number) +1 :
    if  sorted(number[a:b]).pop() == number[b-1] :
        total.append(number[b - 1] - number[a])
        b += 1
        if number[b-1] == number[b-2] :
         a = b
         b += 1
     
    else :
        a += 1
print(total)






