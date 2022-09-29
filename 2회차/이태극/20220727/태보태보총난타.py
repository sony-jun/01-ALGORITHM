#@===@==@=@==(^0^)==@=@===@

left,right=input().split("0")
left_cnt=0
right_cnt=0
for i in left:
    if i=="@":
        left_cnt+=1
for i in right:
    if i=="@":
        right_cnt+=1
print(left_cnt,right_cnt)