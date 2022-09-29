import sys

input = sys.stdin.readline

flist = []
count = 0
for index in range(8): #8x8 체스판이므로 range(8)
    i = ''.join(input().split())
    flist.append(i) #리스트에 입력받은 예제 넣기
    
for i in range(8):
    for j in range(0,8,2): # 0부터 8까지 하되(조건), j를 2씩 증가시키기
        if 'F' == flist[i][j]: #F가 있으면
            count +=1 #count를 더해서 하얀 칸 위에 있는 말의 갯수 구하기

print(count) # 출력