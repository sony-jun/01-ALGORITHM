# A = {1, 2, 4}
# B = {2, 3, 4, 5, 6}

# A-B = {1}
# B-A = {3, 4, 6}

# 개수는 1 + 3 = 4

n_a, n_b = map(int, input().split())    
A = set(map(int, input().split()))      # set이란건 집합을 정의.
B = set(map(int, input().split()))
print(len(A - B) + len(B - A))  # 차집합 연산자는 '-' or 'A.difference(B)'