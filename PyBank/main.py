# import modules
import os
import csv
# Relative path to the data file
path=os.path.join('Resources', 'budget_data.csv')
# Absolute file path to the data file
# path=r'C:\Users\Soni Mohandas\Documents\BootCamp\Python-challenge\PyBank\Resources\budget_data.csv'

# File opened using a variable and is reading with another variable
with open(path) as budget_file:
    file_reader=csv.reader(budget_file, delimiter=',')
# Three list variable one for storing profit or loss and one for storing whole 
# data in two columns and third one for storing for change in profit or loss on every month
    profit_loss=[]
    budget_data=[]
    change=[]
    # Seperating header from data file using next function
    next(file_reader)
    # looping through the file using for loop  
    for i in file_reader:
        budget_data.append(i)           # List stores month and profit or loss
        profit_loss.append(int(i[1]))   # List stores profit or loss only

    # looping through profit or loss list to find the changes   
    for j in range(1,len(profit_loss)):
        change.append(profit_loss[j]-profit_loss[j-1])          # Changes are storing in a list
        budget_data[j].append(profit_loss[j]-profit_loss[j-1])  # Changes are appending in month and profit or loss list as well to match with max/min
    # Finding average change in months
    average_change=round(sum(change)/len(change),2)
    # looping through budget_data list to match maximum change with months and 
    # minimum change with months using conditions
    for k in range(1, len(budget_data)):
        if budget_data[k][2]==max(change):
            max_month=budget_data[k][0]
        if budget_data[k][2]==min(change):
            min_month=budget_data[k][0]

    print(' ')
    print("Financial Analysis")
    print("-------------------------------------------------------")      
    print('')
    print(f'Total months: {len(budget_data)}')          # Printing the total number of months using len fundtion
    print('')
    print(f'Total profit or loss:{sum(profit_loss)}')   # Total profit or loss is calculating
    print('')
    print(f"Average change: {average_change}")          # Printing average changes in profit/loss in the entire period
    print('')
    # Printing greatest increase in profits in the entire period with date
    print(f'Greatest increase in profits: {max_month} (${max(change)})')
    print('')
    # Printing the greatest decrese in losses in the entire period with date
    print(f'Greatest decrease in losses: {min_month} (${min(change)})')
    print('')
# Declare variavle for output file
textfile_path=os.path.join("Analysis", "Analysis.txt")
with open(textfile_path, "w") as txt_file:
    # Writing output to the text file
    txt_file.write("Financial Analysis\n")
    txt_file.write("-------------------------------------------------------\n")
    txt_file.write(f'Total months: {len(budget_data)}\n')
    txt_file.write(f'Total profit or loss:{sum(profit_loss)}\n')
    txt_file.write(f'Greatest increase in profits: {max_month} (${max(change)})\n')
    txt_file.write(f'Greatest decrease in losses: {min_month} (${min(change)})\n')

    