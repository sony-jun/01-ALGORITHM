n = int(input())

numbers = list(map(int,input().split()))
max_ = numbers[0]
min_ = numbers[0]
result=[]
try:
    for i in numbers:
        if i>max_:
            if max_>min_:
                min_ = min_
            else:
                min_ = max_
            max_=i
            result.append((max_-min_))
        else:

            min_ = i
            max_ = i
    print(max(result))
except:
    print(0)