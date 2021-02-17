#find the total number of months,  total amount, average chnage, greatest increase and decrease with dates
#https://www.geeksforgeeks.org/python-generate-successive-element-difference-list/

import os
import csv

pybank_csv = os.path.join("Resources" ,"budget_data.csv")

#need a variable for current month and previous month and the change is profit between those months

dates = []
month_profit = []
monthly_change = []

#total_dates = len(dates)
#net_profit = sum(month_profit)

#smallest_month_change = min(monthly_change)
#avg_change = (sum(monthly_change)/total_dates)

#read in CSV file 

with open(pybank_csv,'r') as csvfile:
    #delimite with commas
    csvreader = csv.reader(csvfile, delimiter =",")
    #skip header 
    next(csvreader, None)

    for row in csvreader:
        dates.append(row[0])
        total_dates = len(dates)
        month_profit.append(int(row[1]))
        total_profit = sum(month_profit)
    
for i in range(len(month_profit)-1):
    monthly_change.append(month_profit[i+1] - month_profit[i])
    
#define final variables outside of loop 

greatst_increase = max(monthly_change)
greatst_decrease = min(monthly_change)
avg_change = sum(monthly_change)/(total_dates - 1)
#return index of the max and min as a date 
max_month = dates[monthly_change.index(max(monthly_change))+1]
min_month = dates[monthly_change.index(min(monthly_change))+1]

    
print(f'Financial Analysis')
print(f'----------------------------')
print(f'Total  Dates: {total_dates}')
print(f'Average Chnage: {avg_change}')
#print("monthly change")
#print(monthly_change)
print(f'greatest profit increase: {greatst_increase} was in {max_month}')
print(f'greatest profit loss: {greatst_decrease} was in {min_month}')




