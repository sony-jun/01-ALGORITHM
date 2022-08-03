from unittest import result


out_result = []
range_result = [i for i in range(1,10001)]
for i in range(10000):
    stri = str(i)
    output = sum(list(map(int,stri)))+i
    out_result.append(output)

# for i in range_result:
#     if i in out_result:
#         range_result.remove(i)

for i in out_result:
    if i in range_result:
        range_result.remove(i)

for i in range_result:
    print(i)