max_length = []
for i in range(3):
    cnt = 0
    cnt_lenghts = []
    number = input()
    for j in range(len(number)-1):
        if number[j] == number[j+1]:
            cnt+=1
            if (j+1) == len(number)-1:
                cnt+=1
                cnt_lenghts.append(cnt)
                cnt = 0
        else:
            cnt+=1
            cnt_lenghts.append(cnt)
            cnt = 0
    max_length.append(max(cnt_lenghts))
print(*max_length,sep='\n')