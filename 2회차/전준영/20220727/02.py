sum=0
answer=0
for i in range(10):
    sum+=int(input())
    if(abs(sum-100)<=abs(answer-100)):
        answer=sum
print(answer)