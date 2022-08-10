t = int(input())
List = []
for i in range(t):
    a,b,c = map(int, input().split(' '))
    if a > b-c :
        List.append('do not advertise')
    elif a < b-c:
        List.append('advertise')
    else:
        List.append('does not matter')
for i in List:
    print(i)