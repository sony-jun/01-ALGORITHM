# 첫째 줄에 문자열의 갯수 N
# M이 주어진다.

#N줄에 있는 5개를 set으로 구성하고.

# S = [
#     "baekjoononlinejudge", "startlink", "codeplus", 
#     "sundaycoding", "codingsh]"
# ]

# words = []
# cnt = 0

# # S랑 Words랑 교집합, 겹치는 게 있는지 체크. 탐색은 in operater로 

# for word in words:
#     if word in S:
#         cnt += 1

# print(cnt)

# # 이렇게 돌리니까 런타임 에러 나네.

# print(len(set(words) & set(S)))

words = []
S = []
cnt = 0


Word_set = set(S)

for word in words:
    if word in set(S):
        cnt += 1

print(cnt)