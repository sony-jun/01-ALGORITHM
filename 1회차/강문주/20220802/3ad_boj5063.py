
case = int(input())

for _ in range(case):
    r, e, c = map(int, input().split())
    if r > e - c:
        print('do not advertise')
    elif r == e - c:
        print('does not matter')
    else:
        print('advertise')
'''
test=int(input())
for i in range(test):
    r, e, c =  map(int, input().split())
    if e - r > c:
        print('advertise')
    elif e - r == c:
        print('dose not matter')
    else:
        print('do not advertise')
'''