# 상근이가 숫자 5를 볼 때, 5로 볼 때도 있지만, 6으로 잘못 볼 수도 있고, 
# 6을 볼 때는, 6으로 볼 때도 있지만, 5로 잘못 볼 수도 있다.

# 두 수 A와 B가 주어졌을 때, 상근이는 이 두 수를 더하려고 한다. 
# 이때, 상근이가 구할 수 있는 두 수의 가능한 합 중, 최솟값과 최댓값을 구해 출력하는 프로그램을 작성하시오.

A, B = map(str, input().split())
# replace 메서드는 문자열 변경 메서드로 str 선언해줌.
min_num = int(A.replace('6', '5')) + int(B.replace('6', '5')) 
max_num = int(A.replace('5', '6')) + int(B.replace('5', '6'))
print(min_num, max_num)