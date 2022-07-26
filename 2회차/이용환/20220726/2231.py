T = int(input())
min_T = T - (len(str(T)) * 9) # 숫자가 너무 커질때 for문 대비, 나올 수 있는 수 중 최소값 구하기
if min_T < 10:
    min_T = 0 # 음수거나 숫자가 너무 작을 경우 에러 혹은 제대로 출력 안됨 방지
for i in range(min_T, T):
    tmp = sum(map(int, str(i)))
    result = tmp + i
    if result == T:
        print(i)
        break
else:
    print(0)