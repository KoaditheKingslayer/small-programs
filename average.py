monthly_spending = [2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 3267.12, 1746.83, 2545.72, 3328.20, 3147.30, 2462.61, 3890.45]
count_items = 0
total = 0
average = 0
constructor = "The average for the numbers: " 

for i in monthly_spending:
    count_items += 1
    total += i
    constructor = constructor + str(i) + ", "

average = total / count_items
constructor = constructor + "is: " + str(average)

print(constructor)
