#!/usr/bin/python3
'''
Lemonade sales in 2 weeks
Profit for each lemonade sold is 1.5$
Tasks:
    1 - Add another day to week 2 through input
    2 - Combine the two lists into 'sales'
    3 - Calculate profit earned on:
    --Best day
    --Worst day
    Seperately and in total
    #hint: use only 3 prints for output
'''

sales_w1 = [7, 3, 42, 19, 15, 35, 9]
sales_w2 = [12, 4, 26, 10, 7, 28]

n = int(input("How much did you make today?: "))
#Add  another day to week 2
sales_w2.append(n)
#Combine both weeks
sales_w1.extend(sales_w2)
#Print calculated profit
print("Profit earned on best day is {}".format(1.5 * (max(sales_w1))))
print("Profit earned on worst day is {}".format(1.5 * (min(sales_w1))))
print("Total profit earned is {}".format(1.5 * (sum(sales_w1))))

