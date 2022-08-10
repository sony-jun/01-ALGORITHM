# dictionary = {
#     'one' : 1,
#     'two' : 10,
#     'three' : 5,
#     'four' : 8,
#     'fice' : 2
# }
# sortdic = sorted(dictionary, key = lambda x:dictionary[x],reverse=True)
# print(sortdic)
numbers = []
numsdic = {}
for i in range(10):
    number = int(input())
    numbers.append(number)
    if number in numsdic:
        numsdic[number] += 1
    else:
        numsdic[number] = 1
avg_num = round(sum(numbers)/len(numbers))
sortdic = sorted(numsdic, key = lambda x : numsdic[x], reverse=True)
print(avg_num,sortdic[0],sep='\n')