from re import A
import sys
sys.stdin = open("성지키기.txt")

# from matrix import *

# 1) 문제이해 : 10min https://www.acmicpc.net/problem/1236
# 모든 열에 한명 이상의 경비원
# 가로m, 세로n // '.'은 빈칸, X는 경비원이 있는칸.
# 첫째 줄에 추가해야 하는 경비원의 최솟값

# 2) 문제 접근 : ..70min (예제 3번으로)
# 행M = 옆으로 그리는거. 가로. / 열N = 세로로 그리는거. 세로.
# 가로 : 행 / 세로 : 열, 헷갈..
# 몇 명의 경비원을 최소로 추가해야 영식이를 만족시키는지를 구하는거면?
# 행/열중에 빈칸의 최대값을 구하는거구나! <<여기까지 1시간걸림.
# X가 없다면 +1, 


# n,m = list(map(int,input().split()))
# countm = 0
# countn = 0
# matrix = [list(input() for i in range(m))]

# for i in range(m):
#     if "X" not in matrix[i]:
#         countm += 1

# for k in range(n):
#     if "X" not in matrix[k]:
#          countn += 1

# print(max(countn,countm))

# # 아...안되겠다. 
# # if "X" not in [array[][] for [] in range[]:
# # for [] 반복문 실행해서 리스트 형식으로 값을 받아온 뒤 리스트에 "X"값이 있는지 확인하는 조건문을 실행하는거구나. 

# n,m = map(int,sys.stdin.readline().split())
# array = [input() for _ in range(n)]

# countm = 0
# countn = 0

# for i in range(n):
#     if "X" not in array[i]:
#         countn += 1


# for k in range(m):
#     if "X" not in [array[][] for k in range(n)]:
#         countm += 1

# print(max(countn,countm))

##이렇게 하니까 vsc에서는 나오는데 런타임에러'난다....아오....
## 2시간이 넘게 걸렸다!!##%@%#$@#$@
## 결국 못풀고 코드리뷰때 이중포문으로 다시 풀어보래서 팀원들꺼 보고 풀었음...젠장.