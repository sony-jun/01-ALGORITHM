S, K, H = map(int, input().split())

l = [S, K, H]
d = {
    S: "Soongsil",
    K: "Korea",
    H: "Hanyang"
}


print("OK" if sum(l) >= 100 else d[min(l)])