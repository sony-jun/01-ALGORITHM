import sys
sys.stdin = open("44_나머지_3052.txt", "r")


# 수를 입력받아 리스트로
num_li = [int(input()) for i in range(10)] # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# key: 나머지, value:수 딕셔너리로
dic = {}
for num in num_li:
    dic[f"{num%42}"] = num

# len(dic)
print(len(dic))