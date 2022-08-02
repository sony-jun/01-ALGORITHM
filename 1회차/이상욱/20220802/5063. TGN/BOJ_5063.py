import sys
sys.stdin = open ('5063.txt')

N = int(input())
dic ={}

for i in range(1, N+1):
    cal = list(map(int, input().split()))

    for j in range(len(cal)):
        dic[j] = int(cal[j])
    # print(dic)
    
    if dic[0] < dic[1] - dic[2]:
        print('advertise')
    elif dic[0] == dic[1] - dic[2]:
        print('does not matter')
    else:
        print('do not advertise')