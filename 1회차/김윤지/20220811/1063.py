




k, s, n = input().split()

kx, ky = 8 - int(k[1]), ord(k[0]) - 65 # king x, y
sx, sy = 8 - int(s[1]), ord(s[0]) - 65 # stone x, y

for _ in range(n):
    move_ = input().upper()
    

