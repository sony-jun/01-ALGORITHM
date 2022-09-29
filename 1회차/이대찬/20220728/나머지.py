import sys

sys.stdin = open("나머지.txt")

lst =[]
for i in sys.stdin:
    a = int(i) % 42
    if a not in lst:
        lst.append(a)
    
print(len(lst))
    
