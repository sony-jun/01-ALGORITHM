# word = input().upper()
# word1 = word
# result = []
# for i in word:
#     result.append(word1.count(i))
#     word1 = word1.replace(i,'')
# # print(result)
# max_result = max(result)
# max_result_index = result.index(max_result)
# if result.count(max_result)>1:
#     print('?')
# else :
#     print(word[max_result_index])

word = input().upper()
specail_word = list(set(list(word)))

result = []
for i in specail_word:
    result.append(word.count(i))

if result.count(max(result))>1:
    print('?')
else:
    print(specail_word[result.index(max(result))])