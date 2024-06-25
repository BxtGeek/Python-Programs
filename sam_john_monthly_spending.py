'''
John has a friend, Sam, who also kept a list of his expenses from last year:

john_monthly_spending = [2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 3267.12, 1746.83, 2545.72, 3328.20, 3147.30, 2462.61, 3890.45]

sam_monthly_spending = [1969.62, 3939.37, 2241.59, 3968.27, 3068.80, 1755.02, 3885.66, 2491.67, 3828.49, 3171.32, 2771.32, 3380.37]

They want to find out how many months John spent more money than Sam. Use a for loop to compare their expenses for each month. Keep track of the number of months where John spent more money.
'''
john_monthly_spending = [2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 3267.12, 1746.83, 2545.72, 3328.20, 3147.30, 2462.61, 3890.45]
sam_monthly_spending = [1969.62, 3939.37, 2241.59, 3968.27, 3068.80, 1755.02, 3885.66, 2491.67, 3828.49, 3171.32, 2771.32, 3380.37]

months_john_spend_more = 0

for i in range(len(john_monthly_spending)):
    if john_monthly_spending[i] > sam_monthly_spending[i]:
        months_john_spend_more += 1

print("months John spent more money than Sam",months_john_spend_more)