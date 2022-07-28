import sys
sys.stdin = open("슈퍼마리오.txt")

#a,b,c = map(int,sys.stdin)

result = 0
tmp = 0 
for i in sys.stdin:
    result += int(i)
    if result < 100:
        tmp += int(i)
    else:
        break

if result - 100 <= abs(tmp - 100):
    print(result)
else:
    print(tmp)
    
        
    
