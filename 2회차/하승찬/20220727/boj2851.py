# 슈퍼 마리오 앞에 10개의 버섯이 일렬로 놓여져 있다. 이 버섯을 먹으면 점수를 받는다.

# 슈퍼 마리오는 버섯을 처음부터 나온 순서대로 집으려고 한다. 하지만, 모든 버섯을 집을 필요는 없고 중간에 중단할 수 있다. 중간에 버섯을 먹는 것을 중단했다면, 그 이후에 나온 버섯은 모두 먹을 수 없다. 따라서 첫 버섯을 먹지 않았다면, 그 이후 버섯도 모두 먹을 수 없다.

# 마리오는 받은 점수의 합을 최대한 100에 가깝게 만들려고 한다.

# 버섯의 점수가 주어졌을 때, 마리오가 받는 점수를 출력하는 프로그램을 작성하시오.

# 받는 값은 10개


score_cnt=[]
abscount=[]
score=0

for i in range(0,10): # 값이 10개라서 인덱스 10개 넣어줌 
    n= int(input())
    score+= n
    score_cnt.append(score)
    s = score -100
    abscount.append(s)

idex=0
ints= abs(abscount[i])
for i in range(0,10): # 
    if abs(abscount[i])<= ints: # 절대값으로 가져오면 .... 인덱스에서 정수값이 아닐때 못찾음 # 순차적으로 진행되기에 앞의 인덱스와 같은값이라면 결과적으로 양수의 인덱스가 ints에 들어가게됨
        ints = abs(abscount[i]) # 
        idex=i
if abscount[i] <= 0: # 안해도 됬었음
    if abscount[i]*-1 in abscount: #그래도 마무리하자면 인덱스 범위 에러가 난다.. 흠.. 조건을 음수일떄로 걸었으니 인덱스를 양수로 바꿔주고 인덱스 안에 값이 있나 확인 후 같은 양수의값이 있다면 다음인덱스를 출력
        print(score_cnt[idex+1])
    else:
        print(score_cnt[idex])
else:
    print(score_cnt[idex])
print(score_cnt[idex])
# # 같은값이 나올경우 높은 수 출력을 위해 인덱스의 앞뒤값을 가져오자.

# # [i-1 ,100] [i+1,100]

# print(score_cnt[idex])

