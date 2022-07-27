import sys

word = sys.stdin.readline()
alpha_dict = {}     ## 알파벳의 개수를 넣을 딕셔너리를 만든다
## 아스키코드를 이용하여 A 부터 Z 까지의 딕셔너리를 만들어준다.
for i in range(65, 91):
    alpha_dict[chr(i)] = 0
## 입력받은 단어로 반복문을 돌린다.
for i in word:
    ## 입력받은 알파벳의 아스키코드가 대문자일 경우
    if 65 <= ord(i) and ord(i) <= 90:
        ## 해당 딕셔너리를 플러스 1
        alpha_dict[i] += 1
    ## 입력받은 알파벳의 아스키코드가 소문자일 경우
    elif 97 <= ord(i) and ord(i) <= 122:
        ## 해당 알파벳의 대문자 딕셔너리에 플러스 1
        alpha_dict[chr(ord(i) - 32)] += 1
#print(alpha_dict)

# for i in word:
#     #print(i)
#     for j in alpha_dict.keys():
#         #print(j)
#         if (ord(i) == ord(j)) or (ord(i) == ord(j) + 32):
#             alpha_dict[j] += 1
# #print(alpha_dict)

## 리스트 컴프리헨션을 이용하여 딕셔너리의 최댓값들로 리스트를 만들어 준다.
max_alpha = [i for i, j in alpha_dict.items() if max(alpha_dict.values()) == j]
## 리스트의 길이가 1 일경우
if len(max_alpha) == 1:
    ## 리스트의 첫째 항 출력
    print(max_alpha[0])
## 리스트의 길이가 1이 아닐경우
else:
    ## ? 출력
    print('?')