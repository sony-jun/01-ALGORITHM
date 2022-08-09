#N 이하인 수 중에서 4와 7로 이루어진 가장 큰수 구하기.
n = int(input())    #N입력받기

for i in range(n, 3, -1): #가장 큰수 구해야함으로 역으로
    if len(str(i)) == str(i).count('4') + str(i).count('7'):
        print(i)
        break

