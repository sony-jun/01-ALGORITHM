numbers = []
for i in range(1, 50): # 배열의 길이가 1000이넘어가니 50으로 설정 #m+1로 해도 된다.
    for j in range(i): #i가 1이면 1번돌고 i가 2이면 2번 돌고
        numbers.append(i)
n, m = map(int, input().split())
listslice = numbers[n-1:m] #슬라이싱
print(sum(listslice)) #sum함수 사용 문제 해결
