import sys
sys.stdin = open("3_슈퍼마리오.txt", 'r')

score = []
total = 0

for i in range(10):
    input_ = int(sys.stdin.readline())
    score.append(input_)

for i in range(len(score)):
    total += score[i]
    if total >= 100: # 두 수가 같으면 그 중 큰 수를 출력한다고 했으니 100보다 커지는 상황만 찾으면 됨
        if abs(100 - total) > abs(100 - (total - score[i])): # 절대값의 차이를 계산해서 전 단계의 절대값이 작은 경우, 즉 100에 가까운 경우만 찾음.
            total -= score[i]
            break

print(total)