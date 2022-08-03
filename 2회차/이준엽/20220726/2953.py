result = []
for i in range(5):
    a,b,c,d = map(int,input().split())
    score = a+b+c+d
    result.append(score)
high_score = max(result)    
print(result.index(high_score)+1,high_score)