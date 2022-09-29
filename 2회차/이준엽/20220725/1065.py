# n = int(input())
# cnt=0
# for i in range(1,n+1):
#     if i<100:
#         cnt+=1
#     elif i>=100 and int(list(str(i))[1])-int(list(str(i))[0]) == int(list(str(i))[2])-int(list(str(i))[1]):
#         cnt+=1
# print(cnt)



n = int(input())
cnt=0

for i in range(1,n+1):
    k = i//10
    if i<100:
        cnt+=1
    elif i>=100 and (k//10) - (k%10) == (k%10) - (i%10) :
        cnt+=1
print(cnt)