import os
import csv
# Absolute file path to the data file
# path=os.path.join('Resources', 'budjet_data.csv')
path=r'C:\Users\Soni Mohandas\Documents\BootCamp\Python-challenge\PyBank\Resources\budget_data.csv'
# File opened using a variable and is reading with another variable
with open(path) as budget_file:
    file_reader=csv.reader(budget_file, delimiter=',')
# Three list variable for storing profit and loss and another one for storing whole 
# data in two columns and third one for storing for change in profit or loss on every month
    profit_loss=[]
    budget_data=[]
    change=[]
    # header section of the file seperating using next function
    next(file_reader)
    # looping through the file and storing whole data and profit or loss alone in two lists
    for i in file_reader:
        budget_data.append(i)
        profit_loss.append(int(i[1]))
    # looping through profit loss list find the changes and storing in another list and it is
    # also appending another list to find max and min change months   
    for j in range(1,len(profit_loss)):
        change.append(profit_loss[j]-profit_loss[j-1])
        budget_data[j].append(profit_loss[j]-profit_loss[j-1])
    # Finding average change in months
    average_change=round(sum(change)/len(budget_data),2)
    # looping through budget_data list to match maximum change with months and 
    # minimum change with months using conditions
    for k in range(1, len(budget_data)):
        if budget_data[k][2]==max(change):
            max_month=budget_data[k][0]
        if budget_data[k][2]==min(change):
            min_month=budget_data[k][0]

    # Printing the total number of months using len fundtion
    print(' ')
    print("Financial Analysis")
    print("-------------------------------------------------------")
        
    print('')
    print(f'Total months: {len(budget_data)}')
    print('')
    # Total profit or loss is calculating
    print(f'Total profit or loss:{sum(profit_loss)}')
    print('')
    # Printing average changes in profit/loss in the entire period
    print(f"Average change: {average_change}")
    print('')
    # Printing greatest increase in profits in the entire period with date
    print(f'Greatest increase in profits: {max_month} (${max(change)})')
    print('')
    # Printing the greatest decrese in losses in the entire period with date
    print(f'Greatest decrease in losses: {min_month} (${min(change)})')
    print('')
    