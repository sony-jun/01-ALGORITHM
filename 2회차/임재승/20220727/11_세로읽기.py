# https://www.acmicpc.net/problem/10798

sero = []
length = []
answer = ''

for i in range(5):
    T = input()
    sero.append(T)
    length.append(len(T))

# m이라는 변수에 0부터 length 배열의 최대값을 넣어주고 반복문을 돌린다
for m in range(max(length)):
    # 받아오는 인풋이 5개이므로 0부터 4까지 5번의 반복문을 돌린다.
    for n in range(5):
        # 만약 m의 값이 n번째 리스트의 길이보다 작다면 리스트의 한 요소씩 더해준다.
        if m < length[n]:
            answer += sero[n][m]

print(answer)