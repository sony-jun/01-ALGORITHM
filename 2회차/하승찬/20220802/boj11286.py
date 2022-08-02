# 절댓값 힙은 다음과 같은 연산을 지원하는 자료구조이다.

# 배열에 정수 x (x ≠ 0)를 넣는다.
# 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. 절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.
# 프로그램은 처음에 비어있는 배열에서 시작하게 된다.
import sys
# sys.stdin = open("input.txt", "r")
import heapq
input= sys.stdin.readline
n= int(input())

x=[]
ax=[]
for __ in range(n):
    command = int(input())

    if len(ax) == 0 and command == 0:  # 길이가 0일때는 0을 출력
        print('0')

# 0일때는 절대값이 낮은 수를 방출 및 출력해야한다.
# 절대값이 1이 이상인 수를 받게되면 push를 통해 리스트에 넣어줘야함
#이때 힙리스트에는 절대값을 넣어주고 일반 리스트에는 일반값을 넣어줘야한다.
    elif abs(command) >=1:       # 입력이 절대값으로 1 이상  # 절대값으로 안하면 입력값이 음수일때 인식을 못함
        acommand = abs(command) # 절대값 커맨드 변수에 넣어준다
        x.append(command)       # 일반정수를 리스트 x에 넣어준다
        heapq.heappush(ax,acommand)# 절대값 커맨드를 리스트ax에 힙푸쉬해준다.
    elif command ==0:           #
        hax =heapq.heappop(ax)  # 절대값 리스트에서  heappop으로 최소값을 가져온다
        ins=[]                  # 임시 리스트를 만들어준 후 heappop으로 가져온 값과 절대값이 같은 값을  x(일반값)리스트에서 가져온다
        for i  in x:
            if abs(i) == hax:
                ins.append(i)   # 절대값과 같은 리스트의 값들을 임시 리스트에 넣는다
        mx= min(ins)            # 임시 리스트 안에서 가장 작은 값을 변수로 지정한 후 출력한다. 출력이 끝나면 일반값x리스트에서 값을 지워준다.
        print(mx)
        x.remove(mx)




# 튜플쌍으로 묶는법
import sys
# sys.stdin = open("input.txt", "r")
import heapq
input= sys.stdin.readline

n= int(input())

x=[]
for __ in range(n):
    command = int(input())

    if len(x) == 0 and command == 0:   
        print('0')
    elif command== 0:               # heappop로 값을 빼내어 인덱스의 두번째값을 출력한다.
        r= heapq.heappop(x)
        print(r[1])                 
    elif abs(command) > 0: # 1 이 아닐시 첫인덱스에 입력의 절대값을 넣고 두번쨰 인덱스에  입력값을 넣어 정렬이 되게 만들어준다.
        heapq.heappush(x,(abs(command),command))


