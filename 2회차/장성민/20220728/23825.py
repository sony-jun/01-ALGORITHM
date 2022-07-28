# S모양 N, A모양 M 입력
s_n, a_m = map(int, input().split())

# 작은 값을 2로 나눈 몫이 sasa의 최댓값
sasa = min(s_n, a_m)

print(sasa // 2)