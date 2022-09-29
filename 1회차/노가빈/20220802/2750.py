list = []
testCase = int(input())
for i in range(testCase):
    list.append(int(input()))
list = set(list)

for i in list:
    print(i)