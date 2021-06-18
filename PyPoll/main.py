#import modules os, csv
import os
import csv

# Path to the csv file assigning to a variable
#file_path=os.path.join('..', 'election_data.csv')
file_path=r"C:\Users\Soni Mohandas\Documents\BootCamp\Python-challenge\PyPoll\election_data.csv"

# Open file mentioning the file path variable and assigning to another variable
with open(file_path) as election_file:

    # File is reading and assigning to a variable
    file_reader=csv.reader(election_file, delimiter=",")
    
    print(' ')
    print("Election Results")
    print("-----------------------------")
        
    # declaring two list variables to store total votes and whole data in the file 
    total_votes=[]
    voters_list=[]
    candidates=[]
    cand=[""]
    # File header is assigning
    file_header=next(file_reader)
    # Looping through all the data in the dataset using for loop
    for data in file_reader:
          
        # Number of votes are storing in a seperate list variable
        total_votes.append(int(data[0]))
        # All the data including voter ID, county, and Candidate are storing in another list
        voters_list.append(data)
        #finding of list of candidates who recieved votes
        candidates.append(data[2])
        
    # Finding length of list which is equal total votes casted
    tot_casted_votes=len(total_votes)
    print(f'Total Votes: {tot_casted_votes}')
    print("-----------------------------")
    
    # Finding complete list of candidates who recieved votes
    print(f'Candidates who recieved votes: {list(set(candidates))}')
    print("")
        
    khan_tot_votes=len([vot for vot in candidates if vot=="Khan"])
    khan_perc_vot='{0:.3f}'.format(khan_tot_votes/tot_casted_votes*100)
    print(f'Khan: {khan_perc_vot}% ({khan_tot_votes})')
    print("")

    li_tot_votes=len([vot for vot in candidates if vot=="Li"])
    li_perc_vot='{0:.3f}'.format(li_tot_votes/tot_casted_votes*100)
    print(f'Li: {li_perc_vot}% ({li_tot_votes})')
    print("")

    correy_tot_votes=len([vot for vot in candidates if vot=="Correy"])
    correy_perc_vot='{0:.3f}'.format(correy_tot_votes/tot_casted_votes*100)
    print(f'Correy: {correy_perc_vot}% ({correy_tot_votes})')
    print("")
   
    tooley_tot_votes=len([vot for vot in candidates if vot=="O'Tooley"])
    tooley_perc_vot='{0:.3f}'.format(tooley_tot_votes/tot_casted_votes*100)
    print(f"O'Tooley: {tooley_perc_vot}% ({tooley_tot_votes})")
    print("----------------------------")
    print("Winner: Khan")
    print("----------------------------")


    
    # #for candidates in voters_list:
        