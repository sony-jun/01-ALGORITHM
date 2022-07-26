# 어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다. 
# 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다. 
# 예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다. 따라서 245는 256의 생성자가 된다. 
# 물론, 어떤 자연수의 경우에는 생성자가 없을 수도 있다. 반대로, 생성자가 여러 개인 자연수도 있을 수 있다.

# 자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오


N = int(input())

c_list = [] # 생성자리스트(constructor list)
for i in range(1, N+1):
    # i를 문자열로 변환하여 순환한 후 int로 변환해서 그것들을 더한다 - map, sum 사용
    # for문 안에 for문 넣는 방법은 이중 for문 이라 시간 많이 소요될 듯
    sum_n = sum(map(int, str(i)))
    d = i + sum_n # 분해합인 decomposition의 약자인 d에 더한 값을 할당
    if d == N:
        c_list.append(i) 

# 문제를 잘 안읽어봤더니 런타임에러가 남
# 자연수 N의 생성자가 없을 수도 있음 즉, 리스트의 길이가 0인 경우는 print(0)
if len(c_list) == 0:
    result = 0
else:
    result = min(c_list)
# else에 그 외의 나머지의 경우는 min값을 찾아 result에 할당하고
# print 한다
print(result)




