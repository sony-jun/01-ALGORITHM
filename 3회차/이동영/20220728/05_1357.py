import sys

sys.stdin = open("input.txt", "r")

def Rev(number):
    
    Rev_number = number[::-1]
   
    for i in range(0,len(Rev_number)):
        if i == 0:
            Rev_number = Rev_number.lstrip('0')
            
    return Rev_number

m, n = input().split()

print(Rev(str(int(Rev(m))+int(Rev(n)))))





