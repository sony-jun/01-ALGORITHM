# import sys
# sys.stdin = open("45_다이얼_5622.txt", "r")

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

# dic: {key: "ABC", val: dial 인덱스 값}
dic = {}
for i in range(len(dial)): # 0, 1, 2, 3, 4, 5 ...
    dic[dial[i]] = i + 3 # {'ABC': 2, 'DEF': 3, 'GHI': 4, 'JKL': 5, 'MNO': 6, 'PQRS': 7, 'TUV': 8, 'WXYZ': 9}

phone_str = "UNUCIC"
result = 0 # 최소 시간

for str in phone_str: # "U", "N" ...
    for k in dic: # dic= "ABC", "DEF", "GHI"... / k="ABC"
        if str in k: # str = "U" / k = "ABC"
            result += dic.get(k) # dic.get(k): 글자 번호에 해당하는 숫자 값

print(result)



# # input값으로 str 받아서, dial 리스트에 있으면 인덱스 값 + 2
# phone_str = input()
# for i in phone_str: # "W", "A"
#     if i in dial:
#         dic[]
# # 최종은 result + len(result): 다이얼 돌리는 데 1초씩 걸리는 듯