N = int(input())

number = 1
result = 0
cnt = 0

while(1):
    if '666' in str(number):
        cnt += 1  #몇번째인지
    if cnt ==  N:
        result = number
        break
    number +=1

print(result)
        
         