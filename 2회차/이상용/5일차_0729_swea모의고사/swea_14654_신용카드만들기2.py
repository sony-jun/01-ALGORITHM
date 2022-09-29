# 1. 카드 번호는 3, 4, 5, 6, 9 로 시작해야 한다.
# 2. 카드 번호에 "-"이 들어갈 수 있으며 "-" 를 제외한 숫자의 개수는 16개이다.
# EX) 6471-6836-9525-5276
# EX) 3029192045012901
# 카드 번호가 주어졌을 때 해당 번호로 신용카드를 만들 수 있는지 판별하는 프로그램을 작성하시오.
# 입력 : 첫 번째 줄에 테스트 케이스의 수 T가 주어진다, 각 테스트 케이스는 한 개의 줄로 이루어지며, 각 줄에는 `자연수`와 `-`로 이루어진 길이가 1 이상인 문자열이 주어진다. 
# 출력 : 각 테스트 케이스마다, 주어진 카드 번호로 신용 카드를 만들 수 있으면 1 만들 수 없으면 0을 출력한다.

# 테스트 케이스 수량 입력
test_case = int(input())

# 리스트에 주어진 카드 번호 넣기
for i in range(test_case):
    number_check = list(map(int, input().split().remove('-')))
    for j in number_check:
        # 신용카드 생성 조건 
        # 1) 첫번째 숫자가 3, 4, 5, 6, 9로 시작해야함 
        # 2) -를 제외한 16자리 수여야함
        if len(number_check) == 16 and (number_check[0] == 3 or number_check[0] == 4 or number_check[0] == 5 or number_check[0] == 6 or number_check[0] == 9) :
            result = 1
        else:
            result = 0
        print('#%d %d' & (i+1, result))
