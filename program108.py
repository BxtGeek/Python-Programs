# 1480. Running Sum of 1d Array

nums = []
count = int(input("Enter the value of count:"))
for i in range(count):
    nums.append(int(input(f"Enter the element {i}:")))

running_sum = 0
for i in range(count):
    running_sum = running_sum + nums[i]
    nums[i] = running_sum   
print(nums)