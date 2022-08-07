# 입력받을 숫자 배열의 개수
for _ in range(int(input())) :

    # 숫자 배열을 리스트로 만들기
    nums = list(map(int, input().split()))

    # 숫자 배열을 내림차순으로 정렬
    nums = sorted(nums, reverse=True)

    # 3번째로 큰 값을 출력
    print(nums[2])