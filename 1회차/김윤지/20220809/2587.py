nums = []
for i in range(5):
    nums.append(int(input()))
    nums.sort()
    #print(nums) #[10, 30, 30, 40, 60]

print(sum(nums)//5) # 평균출력
print(nums[2]) # 5개중에 중앙값 출력
