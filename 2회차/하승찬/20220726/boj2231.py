# 어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 
# N과 N을 이루는 각 자리수의 합을 의미한다. 
# 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다.
#  예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다. 
# 따라서 245는 256의 생성자가 된다. 물론, 어떤 자연수의 경우에는 생성자가 없을 수도 있다. 
# 반대로, 생성자가 여러 개인 자연수도 있을 수 있다.
# 자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.

# 자리수마다 최대값은 9 자리수 * 9를해서 범위를 좁힌다.
n= int(input())

str_n = (len(str(n)))*9
int_n = int(str_n)
lenn= n -int_n # n이 적을때 범위가 음수로 잡혀 미리 처음범위를 정한 후 음수가 나온다면 0부터 시작
if lenn < 0 :
    lenn= 0  # # 자리수마다 최대값은 9 자리수 * 9를해서 범위를 좁힌다.
ncnt =[]
for nums in range(lenn,n+1):# n - 자리수*9 , n+1으로 범위를 잡는다
    sum_conut= 0              #각 자리수를 더해준다
    numss=nums                # 마지막 시행에서 nums의 값이 변하니 nums의 값을 미리 다른 변수로 지정해놓는다.
    while nums != 0:           # while문으로 10으로 나누어 마지막 나머지를 sum_count에 더해준다.
        sum_conut+=nums%10
        nums=nums//10
        if nums ==0:            # nums가 0이되면 break
            break
    if (sum_conut+numss)==n:    # sum_count+미리 지정한 numss의 값이 입력값과 같으면 리스트에 추가해준다
        ncnt.append(numss)

if sum(ncnt)== 0:
    print('0')
else:
    print(min(ncnt))                # ncnt값중에 제일 작은값을 출력한다.


# for i in range(1,n+1): # 최대값이 n을 넘을 수 없기에 n을 순환문의 끝으로 지정 
#     sum_i=0       # 분해합은 n+ n[len]+n[len] 이기에 처음에 순환값을 먼저 넣어준다.
#     while i !=0:            # 10으로 나누어 나오는 나머지값을 sum
#         sum_i+=i%10
#         i= i//10
#         if i ==0:
#             break
#     if sum_i == n:
#         cn.append(i)
#     print(sum_i)
# print(cn)
