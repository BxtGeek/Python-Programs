# 1929. Concatenation of Array

nums = []
ans = []
count = int(input("Enter the value of count: "))
for i in range(count):
    nums.append(int(input(f"Enter element {i}: ")))

ans = nums + nums 
print(ans)

