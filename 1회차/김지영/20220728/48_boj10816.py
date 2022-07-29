n= int(input())    # 상근이 가지고있는 숫자카드 개수
n_list = list(map(int,input().split()))  # 숫자카드에 적혀있는 수
m = int(input())  # 정수 M이 몇개?
m_list = list(map(int,input().split()))  # 정수 M
n_dict = {}

for i in n_list:
    if i not in n_dict:
        n_dict[i] = 1
    else:
        n_dict[i] += 1

for i in m_list:
    if i in n_dict:
        print(n_dict[i],end=' ')
    else:
        print(0, end =' ')