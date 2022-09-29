n = int(input())

for i in range(n):
    r, e, c = map(int, input().split())

    # 광고해서 번 돈에서 광고할 때 드는 비용을 뺀 값이
    # 광고를 안했을 때 가지는 비용보다 크면
    if e - c > r:
        print("advertise")
    # 광고해서 번 돈에서 광고할 때 드는 비용을 뺀 값이
    # 광고를 안했을 때 가지는 비용과 같으면
    elif e - c == r:
        print("does not matter")
    # 광고해서 번 돈에서 광고할 때 드는 비용을 뺀 값이
    # 광고를 안했을 때 가지는 비용보다 작으면
    elif e - c < r:
        print("do not advertise")