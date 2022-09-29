import sys
input = sys.stdin.readline

t = int(input())
for j in range(t):
    n = int(input())
    n_nums = list(map(int,input().split()))
    m = int(input())
    m_nums = list(map(int,input().split()))

    n_nums = set(n_nums)
    for i in m_nums:
        if i in n_nums: ## set으로 찾을때는 상수복잡도 , list로 찾을때는 N복잡도
            print(1)
        else:
            print(0)