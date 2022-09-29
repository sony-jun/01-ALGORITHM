seq = []
for i in range(50):
    seq += [i] * i
    if len(seq) > 1000:
        break
# 입력값의 범위가 1000밖에 안 되기에 1부터 n까지 1000이 넘을 때까지 각자리에 위치하는 리스트를 만들고

a, b = map(int, input().split())
sum = 0
for i in range(a - 1, b):
    sum += seq[i]
print(sum)

# 입력된 두 값 사이의 값들의 합을 구해서 답을 구하였습니다.