dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

word = input()

cnt = 0

for i in range(len(word)) : #input 받은 알파벳 개수만큼 반복
    for j in dial : #dial 리스트 안에서 반복
        if word[i] in j :  #같은 알파벳이 나오면
            cnt += dial.index(j)+3  
#인덱스 위치에서 3을 더해야 시간이 나옴(ABC는 번호 2인데 시간은 3초, 인덱스 위치는 0이기 때문)
print(cnt) #모든 값을 이미 더했으므로 cnt 값만 구하면 된다
