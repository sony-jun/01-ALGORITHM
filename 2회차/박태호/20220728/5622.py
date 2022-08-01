# 다이얼
#숫자 1 = 2초 옆으로 가면 1초 증가

word = input().upper()
#직접 리스트 만듬 
li = [['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']]
# li 길이를 인덱스로 사용
result = 0
for i in li:#['A','B','C'] 상태임 한번 더 각
    for j in i: # 위에서 받아온 리스트의 문자열을 하나씩 뽑아 A B C D~~~~
        #비교를  find? count?? if?.
        # print(j,i)
        for w in word: #입력받은 문자를 순회
            if j == w: #같은 문자를 찾아서 그 인덱스를 추가 할 예정
                result+= int(li.index(i))+3 
# +3 이유는 ABC의 인덱스가 0이라 +2 그리고 ABC는 3초니까 추가로 +1 총 +3
                # result[re_ind]
print(result)
