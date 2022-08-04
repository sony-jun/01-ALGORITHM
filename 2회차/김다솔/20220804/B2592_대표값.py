import sys
sys.stdin = open('B2592.txt')
#첫째 줄 평균, 둘째 줄 최빈값

num = [int(input()) for _ in range(10)]
print(sum(num) // 10)
# print(max(num, key=num.count)) 


s_num = list(set(num)) #[40, 10, 50, 20, 60, 30]
cnt = [] #[2, 1, 1, 1, 2, 3]
for i in range(len(s_num)):
    cnt.append(num.count(s_num[i]))
print(s_num[cnt.index(max(cnt))]) # len(s_num) == len(cnt)