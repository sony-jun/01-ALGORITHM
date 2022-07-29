n, m = map(int, input().split())

list_ = []
for i in range(1, m+1): # 1에서 8까지 반복 
    for j in range(i): # i까지 반복, i가 1이면 1번을 넣어주고 2라면 2를 넣어줌, 반복이 끝나고 다시 아래로 내려갈 떄는 j는 0이 됨
        if len(list_) == m : # 확인해보니 4일때 길이가 7이 되어 멈춤
            break
        list_.append(i) # 이중 반복문을 통해 i만큼 반복하니 리스트에 i숫자가 i만큼 추가 됨

sum_ = sum(list_[n-1:m]) #인덱싱 자리 3~7


