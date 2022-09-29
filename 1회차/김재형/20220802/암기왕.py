# 1
# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5

# T =int(input())

# note = set()
# for t in range(T):
#     N1 = int(input())
#     note1 = list(map(int, input().split()))
#     N2 = int(input())
#     note2 = list(map(int, input().split()))
# for i in range(N1):
#     note.add(note1[i])
#     note.add(note2[i])
# for n in note1:
#     note.remove(n)
# for a in note2:
#     if a in note:
#         print(0)
#     else:
#         print(1)    
#===================================
# T = int(input())
# N_dic = {}

# for i in range(T):
#     N1 = int(input())
#     note1 = list(map(int, input().split()))
#     N2 = int(input())
#     note2 = list(map(int, input().split()))
#     for n in note2:
#         N_dic[n] = 0
#     for n2 in note1:
#         if n2 in N_dic.keys():
#             N_dic[n2] += 1
#     for k, v in N_dic.items():
#         print(v)
# ===========================================
T = int(input())

for i in range(T):
    N1 = int(input())
    note1 = set(map(int, input().split()))
    N2 = int(input())
    note2 = list(map(int, input().split()))
    
    for n in note2:
        if n in note1:
            print(1)
        if n not in note1:
            print(0)