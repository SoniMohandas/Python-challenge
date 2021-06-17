#import modules os, csv
import os
import csv
import numpy as nm
# File path to the csv file assigning to a variable
file_path=r"C:\Users\Soni Mohandas\Documents\BootCamp\Python-challenge\PyBank\Resources\budget_data.csv"

# Open file mentioning the file path variable and assigning to another variable
with open(file_path) as budget_file:

    # File is reading and assigning to a variable
    file_reader=csv.reader(budget_file, delimiter=",")
    
    print(' ')
    print("Financial Analysis")
    print("-------------------------------------------------------")
        
    # declaring a list variable to store profit or loss in the file 
    profit_loss=[]
    tot_data=[]
       
    # File header is assigning
    file_header=next(file_reader)
    # for looping to loop through all the data in the dataset
    for data in file_reader:
          
        # Profit or loss is storing in a seperate list variable
        profit_loss.append(int(data[1]))
        # All the data including dates are storing in another list
        tot_data.append(data)

    # Finding length of the list which is equal total months
    num_months=len(profit_loss)

    # Finding total profit or loss 
    total_profit_loss=sum(profit_loss)

    # Finding the average change of profit or loss in the whole period
    avg_change=round(sum(profit_loss)/num_months,2)

    # Finding the greatest increase in profit 
    grt_increase_profit=max(profit_loss)

    # Finding the greatest decrease in loss
    grt_decrease_loss=min(profit_loss)

    # Using the for loop and conditions finding the dates corresponding to 
    # greatest increase in profits and greatest decrease losses
    for data in tot_data:
        if data[1]==str(grt_increase_profit):
            grt_profit_date=data[0]
            
        if data[1]==str(grt_decrease_loss):
            grt_loss_date=data[0]
     
    # Printing the total number of months and total profit or loss
    print('')
    print(f'Total months: {num_months}')
    print('')
    print(f'Total profit/loss:{sum(profit_loss)}')
    print('')
    print(f"Average change: {avg_change}")
    print('')
    print(f'Greatest increase in profits: {grt_profit_date} (${grt_increase_profit})')
    print('')
    print(f'Greatest decrease in losses: {grt_loss_date} (${grt_decrease_loss})')
    print('')
   

  
        
    