S = input()
cro_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in range(len(cro_list)):
    if cro_list[i] in S:
        S = S.replace(cro_list[i], "*")

print(len(S))



# # 초과초과여야 인정 ,하나가같고 하나가 초과된다해도 등수는 변하지않음 둘다 초과되야됨.. 문제지문대로 풀자.
# n = int(input())

# biggers= []

# for sq in range(n): #값을 리스트 안에 리스트로 넣어준다. 중첩리스트 
#     a,b=map(int,input().split())
#     biggers.append((a,b,1))
    
# print(biggers)
# print(biggers[0][0])

# for i in biggers: # for문으로 자기 리스트를 결합순회해준다,  리스트의 인덱스만 변화하고 비교하는 값은 리스트에 [0],[1]번 리스트를 비교
#     for j in biggers:
#         if i[0] > j[0] and  i[1] > j[1]:
#            [2]+=1

# print(biggers)