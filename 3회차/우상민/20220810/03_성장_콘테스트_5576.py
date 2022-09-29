#백준 콘테스트 5576
#최근 온라인에서의 프로그래밍 콘테스트가 열렸다. W 대학과 K 대학의 컴퓨터 클럽은 이전부터 라이벌 관계에있어,이 콘테스트를 이용하여 양자의 우열을 정하자라는 것이되었다.
# 이번이 두 대학에서 모두 10 명씩이 콘테스트에 참여했다. 긴 논의 끝에 참가한 10 명 중 득점이 높은 사람에서 3 명의 점수를 합산하여 대학의 득점으로하기로 했다.
# W 대학 및 K 대학 참가자의 점수 데이터가 주어진다. 이때, 각각의 대학의 점수를 계산하는 프로그램을 작성하라.

W = [0]*3
K = [0]*3
for i in range(2):
    for idx in range(1, 11):
        if i == 0:
            N = int(input())
            for index in range(1):
                if W[index] - W[index+1] <= 0 and W[index] - W[index+2] <= 0:
                    if W[index] < N:
                        W[index] = N
                    break
                elif W[index+1] - W[index] <= 0 and W[index+1] - W[index+2] <= 0:
                    if W[index+1] < N:
                        W[index+1] = N
                    break
                elif W[index+2] - W[index] <= 0 and W[index+2] - W[index+1] <= 0:
                    if W[index+2] < N:
                        W[index+2] = N
                    break
        else:
            N = int(input())
            for index in range(1):
                if K[index] - K[index+1] <= 0 and K[index] - K[index+2] <= 0:
                    if K[index] < N:
                        K[index] = N
                    break
                elif K[index+1] - K[index] <= 0 and K[index+1] - K[index+2] <= 0:
                    if K[index+1] < N:
                        K[index+1] = N
                    break
                elif K[index+2] - K[index] <= 0 and K[index+2] - K[index+1] <= 0:
                    if K[index+2] < N:
                        K[index+2] = N
                    break

print(sum(W), sum(K))
