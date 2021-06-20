#import modules os, csv
import os
import csv

# Path to the csv file assigning to a variable
#file_path=os.path.join('Resources', 'election_data.csv')
file_path=r"C:\Users\Soni Mohandas\Documents\BootCamp\Python-challenge\PyPoll\Resources\election_data.csv"

# Open file mentioning the file path variable and assigning to another variable
with open(file_path) as election_file:

    # File is reading and assigning to a variable
    file_reader=csv.reader(election_file, delimiter=",")
    
    print(' ')
    print("Election Results")
    print("-----------------------------")
        
    # declaring two list variables to store total votes and candidates in the file 
    total_votes=[]
    candidates=[]

    winner={}
    
    # File header is assigning
    file_header=next(file_reader)
    # Looping through all the data in the dataset using for loop
    for data in file_reader:
          
        # Number of votes are storing in a seperate list variable
        total_votes.append(int(data[0]))
       
        #finding of list of candidates who recieved votes
        candidates.append(data[2])
        
    # Finding length of list which is equal total votes casted
    tot_casted_votes=len(total_votes)
    print(f'Total Votes: {tot_casted_votes}')
    print("-----------------------------")
    
    # Finding complete list of candidates who recieved votes
    print(f'Candidates who recieved votes: {list(set(candidates))}')
    print("")

    # Finding total votes got by Khan using comprehenson of for loop and conditions    
    khan_tot_votes=len([vot for vot in candidates if vot=="Khan"])
    # Finding percentage of votes got and formating to 3 decimal places
    khan_perc_vot='{0:.3f}'.format(khan_tot_votes/tot_casted_votes*100)
    # printig the percentage of votes Khan got
    winner.update({"Khan":khan_perc_vot})
    # Printing the results of Khan
    print(f'Khan: {khan_perc_vot}% ({khan_tot_votes})')
    print("")

    # Finding total votes got by Li using comprehenson of for loop and conditions
    li_tot_votes=len([vot for vot in candidates if vot=="Li"])
    # Finding percentage of votes got and formating to 3 decimal places
    li_perc_vot='{0:.3f}'.format(li_tot_votes/tot_casted_votes*100)
    # printig the percentage of votes LI got
    winner.update({"Li":li_perc_vot})
    # Printing the results of Li
    print(f'Li: {li_perc_vot}% ({li_tot_votes})')
    print("")

    # Finding total votes got by Correy using comprehenson of for loop and conditions
    correy_tot_votes=len([vot for vot in candidates if vot=="Correy"])
    # Finding percentage of votes got and formating to 3 decimal places
    correy_perc_vot='{0:.3f}'.format(correy_tot_votes/tot_casted_votes*100)# printig the percentage of votes Khan got
    # printig the percentage of votes Correy got
    winner.update({"Correy":correy_perc_vot})
    # Printing the results of Correy
    print(f'Correy: {correy_perc_vot}% ({correy_tot_votes})')
    print("")
   
    # Finding total votes got by O'Tooley using comprehenson of for loop and conditions
    tooley_tot_votes=len([vot for vot in candidates if vot=="O'Tooley"])
    # Finding percentage of votes got and formating to 3 decimal places
    tooley_perc_vot='{0:.3f}'.format(tooley_tot_votes/tot_casted_votes*100)
    # printig the percentage of votes O'Tooley got
    winner.update({"O'Tooley":tooley_perc_vot})
    # Printing the results of O'Tooley
    print(f"O'Tooley: {tooley_perc_vot}% ({tooley_tot_votes})")
    
    # finding the matching max value from the winner dictionery
    win_match=max(winner,key=winner.get)
    print("----------------------------")
    print(f'Winner: {win_match}')
    print("----------------------------")
    print(" ")

        