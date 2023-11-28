# Write a program to find the sum of the given series 1+2+3+ . . . . . .(N terms) 

nums= []
count = int(input("Enter the value you need in series:"))
for i in range(count):
    nums.append(int(input(f"Enter the {i} element:")))

series_sum = 0
for i in range(count):
    series_sum = series_sum + nums[i]

print("Sum of Series is",series_sum)