#백준 가장 큰 금민수 1526
#은민이는 4와 7을 좋아하고, 나머지 숫자는 싫어한다. 금민수는 어떤 수가 4와 7로만 이루어진 수를 말한다.
# N이 주어졌을 때, N보다 작거나 같은 금민수 중 가장 큰 것을 출력하는 프로그램을 작성하시오.
answer = []
N_1 = input()
N = list(map(str, N_1))
if N[0] == '4':
    if '0' not in N and '1' not in N and '2' not in N and '3' not in N :
        for i in range(0, len(N)):
            if 4 > int(N[i]) >= 0:
                N[int(i)] = 7
            elif 7 > int(N[i]) >= 4:
                N[int(i)] = 4
            elif 10 > int(N[i]) >= 7:
                N[int(i)] = 7
            answer.append(N[int(i)])
    else:
        N.pop()
        for i in range(0, (len(N))):
            if 4 >= int(N[i]) >= 0:
                N[int(i)] = 7
            elif 7 > int(N[i]) > 4:
                N[int(i)] = 4
            elif 10 > int(N[i]) >= 7:
                N[int(i)] = 7
            answer.append(N[int(i)])

elif N[0] != '4':
    if N[0] == '0':
        N[0] = ''
    elif N[0] == '1':
        N[0] = ''
    elif N[0] == '2':
        N[0] = ''
    elif N[0] == '3':
        N[0] = ''
    elif N[0] == '5':
        N[0] = 4
    elif N[0] == '6':
        N[0] = 4
    elif N[0] == '7':
        N[0] = 7
    elif N[0] == '8':
        N[0] = 7
    elif N[0] == '8':
        N[0] = 7
    elif N[0] == '9':
        N[0] = 7
    answer.append(N[0])
    for i in range(1, (len(N))):
        if 4 > int(N[i]) >= 0:
            N[int(i)] = 7
        elif 7 > int(N[i]) >= 4:
            N[int(i)] = 4
        elif 10 > int(N[i]) >= 7:
            N[int(i)] = 7
        answer.append(N[int(i)])
if int(N_1) < 44:
    if int(N_1) >= 7 :
        answer.clear()
        answer.append('7') 
    elif 7> int(N_1) >= 4:
        answer.clear()
        answer.append('4') 
print(*answer,sep='')




