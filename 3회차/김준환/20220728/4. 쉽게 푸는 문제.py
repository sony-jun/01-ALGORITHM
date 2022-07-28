# 수열의 번호 주어짐 -> 인덱스 + 1
# 구간 [] 로 수열 리스트에서 잘라오면 됨
# sum으로 합 구하기

# s,e = map(int,input().split())
# lst = ''
# for i in range(1,e):
#     lst += str(i)*i
# num_lst = list(map(int,lst[s-1:e]))
# print(num_lst)
# print(str(sum(num_lst)))





# 다른 사람의 코드
a,b = map(int,input().split())
 
arr = [0]
for i in range(46):
    for j in range(i):
        arr.append(i)
 
print(sum(arr[a:b+1]))