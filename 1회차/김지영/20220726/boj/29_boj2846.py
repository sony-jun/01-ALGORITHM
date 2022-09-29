# 오르막길
# 상근이 안녕~!
# 자전거 길은 오르막길, 내리막길, 평지로 이루어져있다.
# 일정거리마다 높이 측정, y축의 변화?
# 가장 큰 오르막길의 크기를 구한다
# 높이는 길이가 N인 수열, 
# 오르막길 = 2개의 수로 이루어진 높이가 증가하는 부분 수열
# 오르막길크기 = 부분 수열[len(부분수열)-1] - 부분 수열[0]
lenT = int(input())
T = list(map(int,input().split()))
up = 0 # 올라간 높이의 합
r = []
# 이렇게 되면 결국 저 lenT는 T에서 하는 일이 없어요
# swea였으면 분명 T에다가 lenT보다 많은 값을 집어넣는 인간들이 있을거라구요
# 특정 크기를 갖는 배열에 띄어쓰기로 요소값을 어떻게 집어넣냐고요

# 오르막길은 오르막길 부분 수열의 처음과 마지막을 빼도 되지만
# 올라가는 부분부분의 길이를 구해서 더해도 구할 수 있습니다.
# 그리고 부분 수열을 굳이 만들지 않아도 된다면 만들고싶지 않아요.
# 그리고 크기가 정해진 배열에 인풋하는 방법은 도저히 모르겠으니까
# 오르막길 오르는 배열의 범위를 lenT로 정해버릴게요.
# 그러면 배열을 아무리 많이 써도 lenT만큼만 읽겠죠.
for i in range(1,lenT):
    if T[i]>T[i-1]:         # 오르막길입니까?
        up = up + T[i] - T[i-1]   # 오르막길의 부분길이의 합
        if i == lenT-1:     # 오르막길 도중 배열의 맨 끝에 도달하면
            r.append(up)    
    else:                   # 오르막길이 아닐때
        r.append(up)         # 구한 up을 넣고,
        up = 0              # 오르막길의 총합  초기화
print(max(r))       # 오르막길의 부분 합 중 가장 큰것을 구해라
