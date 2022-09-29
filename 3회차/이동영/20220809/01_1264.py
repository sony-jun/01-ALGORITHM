import sys

sys.stdin = open("input.txt", "r")

list_ = ['a','A','e','E','i','I','o','O','u','U']

while True:
            
    temp_ = input()
    cnt = 0
    
    if temp_ == '#':
        break
    
    for i in temp_:
        if i in list_:
            cnt += 1
    
    print(cnt)   