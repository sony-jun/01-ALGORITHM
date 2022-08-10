t = int(input())
printlist = []
for i in range(t):
    str = list(input().split(' '))
    index = int(str[0])
    lst = list(str[1])
    del lst[index-1]
    printlist.append(''.join(lst))
for str in printlist:
    print(str)

