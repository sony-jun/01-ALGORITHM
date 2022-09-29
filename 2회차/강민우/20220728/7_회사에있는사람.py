N = int(input())
result ={}

for a in range(N) :
    name, log = input().split()
    result[name] = log
    if result[name] == 'leave' :
        del result[name]
new_result = sorted(result.keys(), reverse =True)

for a in new_result :
    print(a)




