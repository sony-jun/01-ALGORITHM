# 번호순으로 나열할 수 있는지 여부를 알려주는 프로그램을 작성해 주자.
# 스택 # ad-hoc

N, M = map(int,input().split())
l = []
st_list = []
for i in range(M):
    k = int(input())
    kn = list(map(int,input().split()))
    st_list.append(kn.pop())
print(st_list)
