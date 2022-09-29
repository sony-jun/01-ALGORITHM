n = int(input())
n1 = n
cnt=0
while 1:
    origin_sum = n//10+n%10
    new_num = (n%10*10)+(origin_sum%10)
    n = new_num
    cnt+=1
    if new_num == n1:
        break
print(cnt)