'''
John has a list of his monthly expenses from last year:
monthly_spending = [2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 3267.12, 1746.83, 2545.72, 3328.20, 3147.30, 2462.61, 3890.45]
He wants to know his average expenses for each semester. Using a for loop, calculate John’s average expenses for the first semester (January to June) and the second semester (July to December).
'''
monthly_spending = [2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 3267.12, 1746.83, 2545.72, 3328.20, 3147.30, 2462.61, 3890.45]

first_sem_total = 0
second_sem_total = 0

for i, value in enumerate(monthly_spending):
    if i < 6:
        first_sem_total += value
    else:
        second_sem_total += value
        
first_sem_avg = first_sem_total/6
second_sem_avg = second_sem_total/6

print("Average expenses for First semester",first_sem_avg)
print("Average expenses for Second semester",second_sem_avg)