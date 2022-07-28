N = int(input())
number =  input().split()
M = int(input())
number_2 = input().split()
total = {}

for a in number :
    total[a] = total.get(a,0) + 1
    
for a in number_2 :
    if a in total.keys() :
        print(total[a], end =' ')
    else :
        print(0 , end = ' ')
    
