numbers = []
for i in range(1, 50): # 배열의 길이가 1000이넘어가니 50으로 설정
    for j in range(i): #i가 1이면 1번돌고 i가 2이면 2번 돌고
        numbers.append(i)
n, m = input().split()
listslice = numbers[int(n)-1:int(m)] #슬라이싱
print(sum(listslice)) #sum함수 사용 문제 해결
