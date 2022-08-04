n = int(input())
seet = []

for _ in range(n):
    line = (list(input()))
    seet.append(line)
# 입력되는 각 줄을 라인이라는 리스트에 넣어주고 빈 시트에 주어진 n번 만큼 입력하여 n*n의 매트릭스를 만들어 줍니다.

line_cnt = 0
for i in range(n):
    cnt = 0
    # 각 줄을 순회하며 확인합니다.
    for j in range(n):
        if seet[i][j] == '.':
            cnt += 1
            # '.'이 연속한 길이를 알기위해 '.'이 나올때마다 1씩 추가해줍니다.
        elif seet[i][j] == 'X':
            if cnt >= 2:
                line_cnt += 1
            cnt = 0
            # 'X'가 나왔을때 이전까지 나온 '.'의 누적합이 2이상이면 line에 누울 자리가 하나 
            # 나온것이므로 1을 추가해주고 뒤를 확인해야하기 때문에 cnt를 0부터 다시 시작하기위해 0을 반환합니다.
    if cnt >= 2:
        line_cnt += 1
    # 마지막 자리가 '.'으로 끝났을경우 몇번의 연속된 값이 있었는지 확인해줍니다.
# 반복이 끝나면 가로줄을 기준으로 누울 자리 값이 나오게 됩니다.

stripe_cnt = 0
for i in range(n):
    stripe = []
    cnt = 0
    for j in range(n):
        stripe.append(seet[j][i])
        # n*n의 형태이기에 n행이면 n열의 문자열이 주어질것입니다.
        # 그래서 각 행을 순회하며 i자리에 있는 값들을 모아 자릿값의 열을 구하여줍니다.
    
    for k in range(n):
        if stripe[k] == '.':
            cnt += 1
        elif stripe[k] == 'X':
            if cnt >= 2:
                stripe_cnt += 1
            cnt = 0
    if cnt >= 2:
        stripe_cnt += 1
# 각 열마다 행에서 누울 자리를 찾은 것처럼 누울 자리를 찾아 줍니다.
print(line_cnt, stripe_cnt)
# 가로와 세로의 누울자리 값을 출력해줍니다.