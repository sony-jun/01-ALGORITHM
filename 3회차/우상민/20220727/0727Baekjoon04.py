# 슈퍼 마리오 앞에 10개의 버섯이 일렬로 놓여져 있다. 이 버섯을 먹으면 점수를 받는다.

# 슈퍼 마리오는 버섯을 처음부터 나온 순서대로 집으려고 한다. 하지만, 모든 버섯을 집을 필요는 없고 중간에 중단할 수 있다. 중간에 버섯을 먹는 것을 중단했다면, 그 이후에 나온 버섯은 모두 먹을 수 없다. 따라서 첫 버섯을 먹지 않았다면, 그 이후 버섯도 모두 먹을 수 없다.

# 마리오는 받은 점수의 합을 최대한 100에 가깝게 만들려고 한다.

# 버섯의 점수가 주어졌을 때, 마리오가 받는 점수를 출력하는 프로그램을 작성하시오.
point = []
for i in range(10):
    N = int(input())
    point.append((N))
count = 0
for idx in range(1, 11):
    count += point[idx-1]
    A = 100 - (count + point[idx])
    B = 100 - count
    if idx == 10:
        if A < B:
            print(count)
    elif abs(A) > abs(B):
        break
print(count)

#100에서 count를 빼준 값이 작을 수록 가까움
#실패 내일 다시 봐야할듯...




