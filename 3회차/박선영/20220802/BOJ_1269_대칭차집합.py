# A의 원소개수 an, B의 원소개수 bn
an, bn = map(int, input().split())
# A집합과 B 집합
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 두 리스트를 합치고 set으로 중복을 2번 제거하여 길이 출력할 거임
# 두 리스트의 중복 개수: (an + bn) - len(set(A + B))
# 원래 리스트에서 중복 개수를 2번 빼기: (an + bn) - 2 * ((an + bn) - len(set(A + B)))
# 위 계산을 정리하면 아래처럼 됨
print(2 * len(set(A + B)) - (an + bn))