from unittest import result


N , M =map(int , input().split())
result_list = {}
result = []

for a in range(N + M) :
    info = input()
    result_list[info] = result_list.get(info,0) +1

for a in result_list.keys() :
    if result_list[a] == 2 :
        result.append(a)

result.sort()

print(len(result),'\n'.join(result))


    

