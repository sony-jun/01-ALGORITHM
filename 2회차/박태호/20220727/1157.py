words = input().upper()          # MISSISSIPI  
set_word = list(set(words))   # [M, P, I, S]
li = []

for i in set_word:          # 순회
    cnt = words.count(i)
    li.append(cnt)
    
if li.count(max(li)) > 1: # 최대값이 1개보다 많으면 
    print('?')

else:
    print(set_word[li.index(max(li))])   
    # li의 최대값의 인덱스인데 li의 인덱스고 set_word인덱스로 접근