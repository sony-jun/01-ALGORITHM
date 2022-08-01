# 수열의 번호 주어짐 -> 인덱스 + 1
# 구간 [] 로 수열 리스트에서 잘라오면 됨
# sum으로 합 구하기

# s,e = map(int,input().split())
# lst = ''
# for i in range(1,e):
#     lst += str(i)*i
# num_lst = list(map(int,lst[s-1:e]))
# print(num_lst)
# print(sum(num_lst))



s,e = map(int,input().split())
 
lst = [0]
for i in range(1,46):
    for j in range(i):
        lst.append(i)
 
print(sum(lst[s:e+1]))
