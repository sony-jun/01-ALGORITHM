# 두 수를 입력받는다
# 각 숫자의 인수를 구한다.
# 1부터 입력한 숫자까지 각 숫자에서 나머지가 0이 아닐때까지 나누어 카운트 한 후 다음 숫자로 넘어가게
# 딕셔너리에 키와 값으로 인수와 제곱수를 기록한다
# 최대공약수는 각 딕셔너리에서 키가 같이 존재하는 키만 불러온 후 둘 중에 작은 값 제곱
# 최소공배수는 각 딕셔너리 모든 키 종류 다 불러와서 중복은 큰 값으로 제곱

def Insu(num):                            # 입력한 값의 인수를 모두 구하는 함수
    dic = {1:1}
    if num == 1:
        return dic
    for n in range(2,num+1):
        cnt = 0
        while num%n == 0 and n <= num:
            num//=n
            cnt += 1
            dic[n]=cnt
    return dic

num_1, num_2 = map(int,input().split())                 # 두 수 입력

insu_1 = Insu(num_1) # 첫 번째 숫자 인수
insu_2 = Insu(num_2) # 두 번째 숫자 인수

g_yak = {}
g_bae = {}

for n in insu_1:
    if n in insu_2:
        g_yak[n]=min(insu_1[n], insu_2[n])
        g_bae[n]=max(insu_1[n], insu_2[n])
    else:
        g_bae[n]=insu_1[n]
for n in insu_2:
    if n in insu_1:
        g_yak[n]=min(insu_1[n], insu_2[n])
        g_bae[n]=max(insu_1[n], insu_2[n])
    else:
        g_bae[n]=insu_2[n]
yak = 1
for i in g_yak:
    yak *= i**g_yak[i]
bae = 1
for i in g_bae:
    bae *= i**g_bae[i]

print(yak)
print(bae)