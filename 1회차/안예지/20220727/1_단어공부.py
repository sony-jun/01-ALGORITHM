# 1157. 단어 공부
"""
알파벳 대소문자로 된 단어가 주어지면, 
이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
단, 대문자와 소문자를 구분하지 않는다.

# 입력
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 
주어지는 단어의 길이는 1,000,000을 넘지 않는다.

# 출력
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 
단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

# 접근
1. 주어진 문자열을 순회하며 딕셔너리를 만든다.
2. 딕셔너리 키 중에서 제일 값이 높은 요소를 골라 리스트로 만든다.
3. 리스트의 길이가 1을 초과할 경우(
    가장 많이 사용된 알파벳이 여러 개 존재
)
4. '?'를 출력한다.

"""
# word = input()
# word_dict = {}
# for i in word:
#     word_dict[i] = word_dict.get(i, 1) + 1
# max_list = sorted(word_dict.values(), reverse = True)
# if max_list[0] == max_list[1]:
#     print('?')
# else:
#     print(max_list[0])
    
# 대소문자 구분을 안 한다.
# ord()로 숫자로 바꿔준 후, 
# 같은 숫자를 문자로 하는 키로 만들어서
# 딕셔너리 만들고 똑같이

word = list(map(ord, input()))
# print(word) # 정상 작동
key_l = []
num_dict = {}
for i in word:
    if i > 90:
        key_l += [str(int(i) - 32)]
    else: 
        key_l += [str(i)]
# print(key_l)
for chr in key_l:
    num_dict[chr] = num_dict.get(chr, 0) + 1
# print(num_dict)
# max_list = sorted(num_dict.values(), reverse = True)
# if len(max_list) == 1:
#     print(max_list[0])

# elif max_list[0] == max_list[1]:
#         print('?')
# else:
#     print(max_list[0])

# 틀림.
# 그럼 max를 구해서 그 수를 리스트랑 비교해보는 수밖에 없음.
# count_list = list(num_dict.values())
# if len(count_list) == 1:
#     print('1')
# # print(count_list)
# max_num = max(count_list)
# cnt = 0
# for i in count_list:
#     if i == max_num:
#         cnt += 1
#         if cnt > 1:
#             print('?')
#         else:
#             print(max_num)
# 역시 틀림.
        
        
    





