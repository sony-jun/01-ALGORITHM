# 쉽게 푸는 문제
A, B = map(int, input().split()) 
# 3 7이면
# 1+2+2+3+3+3+4+4+.........
# 1 2 3 4 5 6 7
#     2 3 3 3 4 = 15 
# #반복문으로 수열을 만들어야 하는데 
# re = []
# for i in range(1,B+1):# 수열먼저 7번 반복예정
#     for j in range(i):
#         re.append(i)

# print(sum(re[A-1:B])) # [2,3,3,3,4]


#다른풀이 while 이용하여 풀이
num_list = []
n = 1

while len(num_list) < B:     # 길이가 B보다 작을 때
    for _ in range(n):       # n만큼 반복인데 계속 증가할거임
        num_list.append(n) 
    n += 1                   # 1 증가하여 1,2,2,3,3,3... 이런식으로 만들었다.
    # 하지만 전체 길이가 10이다 B는 7인데 무슨 일인가?
    # 이유는 숫자 3까지 반복했을 때 길이가 6이고 숫 4 반복으로 넘어가기 때문이다. 
print(num_list)