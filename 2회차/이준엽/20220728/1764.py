n,m = map(int,input().split())

dic = dict()
for i in range(n):
    no_ear = input()
    dic[no_ear] = '듣도못한사람'

result=[]

for i in range(m):
    no_eye = input()
    if no_eye in dic:
        result.append(no_eye)

result.sort()

print(len(result),*result,sep='\n')

# n, m =map(int,input().split())

# no_eyes = []
# no_ears = []
# no_ears_eyes = []
# result = {
# }

# for i in range(n):

#     noear = input()
#     no_ears.append(noear)
#     result[noear] = 0

# for i in range(m):

#     noeye = input()
#     no_eyes.append(noeye)
#     result[noeye] = 0

# for i in no_eyes:
    
#     result[i]+=1

# for i in no_ears:

#     result[i]+=1

# for k, v in result.items():
#     if v == 2:
#         no_ears_eyes.append(k)
# no_ears_eyes.sort()
# print(len(no_ears_eyes))
# for i in no_ears_eyes:
#     print(i)



# n, m = map(int,input().split())
# ears = []
# eyes = []
# result = {
# }
# real_result = []
# for i in range(n):
#     ear = input()
#     ears.append(ear)
#     result[ear] = 0

# for i in range(m):
#     eye = input()
#     eyes.append(eye)
#     result[eye] = 0

# for i in ears:
#     result[i] += 1
# for i in eyes:
#     result[i] += 1

# for k, v in result.items():
#     if v == 2:
#         real_result.append(k)
# real_result.sort()
# print(len(real_result))
# for i in real_result:
#     print(i)




### 2.


# n,m=map(int,input().split())
# n_list=set()
# m_list=set()
# #nm_list=[]
# cnt=0
# for i in range(n):
#     name=input()
#     n_list.add(name)
# for i in range(m):
#     name=input()
#     m_list.add(name)

# nm_list=sorted((n_list&m_list)) ## n_list랑 m_list들 중에서 같은값만 있는걸로 반환
# print(len(nm_list))
# for i in range(len(nm_list)):
#     print(nm_list[i])



##### 3.


# n, m = map(int, input().split())
# not_hear = []
# not_see = []
# temp = []
# result = []

# for _ in range(n):
#     s = input()
#     not_hear.append(s)

# for _ in range(m):
#     s = input()
#     not_see.append(s)

# temp = not_hear + not_see
# temp.sort()

# for i in range(1, n + m):
#     if temp[i] == temp[i - 1]:
#         result.append(temp[i])

# print(len(result))
# for i in result:
#     print(i)