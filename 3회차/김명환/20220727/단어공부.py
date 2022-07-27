# word = input().upper()
# char = {}
# for i in word:
#     if i not in char:
#         char[i] = 1
#     else :
#         char[i] +=1
# #key값에 lambda 함수(무명함수) 사용 -> 매개변수와 결과값 vlaue 값 중심으로 정렬
# char = sorted(char.items(), key = lambda x:x[1], reverse=True) 
# if char[0] == char[1] :
#     print('?')
# else:
#     print(max(char,key=char.get))
word = input().upper()
# 단어에서 중복되는 알파벳 제거 후 리스트에 저장
word_list = list(set(word))
cnt_list = [] # 카운트 저장하기 위한 리스트 
# 중복후 저장된 리스트에서 하나씩 word와 비교하며 카운트한 뒤 해당 카운트 수를 리스트에 저장 
for i in word_list:
    cnt_list.append(word.count(i))  
# 카운트 리스트에서 max (최댓값)의 수를 세고 그 카운트 한 수가 1보다 클때    
if cnt_list.count(max(cnt_list)) > 1 :  # count 숫자 최대값이 1보다 클때
    print('?') 
else: 
    print(word_list[cnt_list.index(max(cnt_list))])
