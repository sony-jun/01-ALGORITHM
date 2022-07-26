#"나는 요리사다"는 다섯 참가자들이 서로의 요리 실력을 뽐내는 티비 프로이다. 각 참가자는 자신있는 음식을 하나씩 만들어오고, 서로 다른 사람의 음식을 점수로 평가해준다. 
# 점수는 1점부터 5점까지 있다.
# 각 참가자가 얻은 점수는 다른 사람이 평가해 준 점수의 합이다. 이 쇼의 우승자는 가장 많은 점수를 얻은 사람이 된다.
# 각 참가자가 얻은 평가 점수가 주어졌을 때, 우승자와 그의 점수를 구하는 프로그램을 작성하시오.
# 2953
a = map(int,input().split())
b = map(int,input().split())
c = map(int,input().split())
d = map(int,input().split())
e = map(int,input().split())
a = sum(a)
b = sum(b)
c = sum(c)
d = sum(d)
e = sum(e)
fst = max(a,b,c,e,d)
list_ = [a,b,c,d,e] 
print(list_.index(fst)+1,fst)