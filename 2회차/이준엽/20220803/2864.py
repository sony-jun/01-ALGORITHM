a, b = map(int,input().split())

sa = str(a)
sb = str(b)

max_sum = int(sa.replace('5','6'))+int(sb.replace('5','6'))
min_sum = int(sa.replace('6','5'))+int(sb.replace('6','5'))

print(min_sum,max_sum)