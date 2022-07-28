# 10816번 숫자카드 2

# 첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다.
N = int(input())
# 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다.
N_num = list(map(int, input().split()))
# 셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다.
M = int(input())
# 넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어지며, 
# 이 수는 공백으로 구분되어져 있다.
M_num = list(map(int, input().split()))

# N_num에 들어있는 수 세고 기록할 딕셔너리
count_dict = {}

for i in N_num :
    # 만약 i가 count_dict에 있으면 밸류에 1 더하기
    if i in count_dict :
        count_dict[i] += 1
    # 없으면 i를 키로 하고 밸류에 1을 넣어준다.
    elif i not in count_dict :
        count_dict[i] = 1

# M_num에 들어있는 수 count_dict에 있는지 확인하고 값 가져와 담을 리스트
count_list = []

for j in M_num :
    # M_num에 있는 수가 N_num에도 있는 경우
    if j in count_dict :
        count_list.append(count_dict[j])
    else:
        count_list.append(0)

print(*count_list)
