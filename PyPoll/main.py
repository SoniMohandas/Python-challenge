#import modules 
import os
import csv

# Path to the csv file is assigning to a variable
file_path=os.path.join('Resources', 'election_data.csv')
# file_path=r"C:\Users\Soni Mohandas\Documents\BootCamp\Python-challenge\PyPoll\Resources\election_data.csv"

# Open file and assigning to a variable
with open(file_path) as election_file:
    # File is reading and assigning to a variable
    file_reader=csv.reader(election_file, delimiter=",")
        
    # declaring one list variable to store candidates names as equal to the number of votes they got
    # and a dictionary variable to store candidate name and number of votes they got. 
    candidates=[]
    winner={}
    
    # File header is assigning to start from second row when looping through data file
    file_header=next(file_reader)
    # Looping through all the data in the dataset using for loop
    for data in file_reader:
             
        # Candidates names are assigning to a list, each candidate names will be stored 
        # which is equal to the number of votes they got
        candidates.append(data[2])
        
    # Finding length of candidate list which is equal to total votes polled
    tot_casted_votes=len(candidates)
    # candidates list is cleaning, ie eliminating duplicate values and storing exact candidate 
    # list in another variable.  In it candidates names appears only ones
    list_cand= list(set(candidates))

    print(' ')
    print("Election Results")
    print("-----------------------------")
    print(f'Total Votes: {tot_casted_votes}')  # printing total votes polled
    print("-----------------------------")
    print("")
    
    # looping through all the candidate names using for loop
    for i in range(len(list_cand)):
        # Finding total votes got by each candidate using for loop comprehension and condition
        # here in the inner for loop the candidate names appears in candidate list as equal to the 
        # the votes they got
        votes_got=len([vot for vot in candidates if vot==list_cand[i]])
        # Finding percentage of votes got and formating to 3 decimal places
        perc_vot='{0:.3f}'.format(votes_got/tot_casted_votes*100)
        # adding percentage of votes to the dictionary with candidate name as key
        winner.update({list_cand[i]:perc_vot})
        # Printing the results of each candidate's name percentage of votes they got and number of votes they got
        print(f'{list_cand[i]}: {perc_vot}% ({votes_got})')
        print("")
 
    # finding the matching key with the max value from the winner dictionery
    win_match=max(winner,key=winner.get)
    print("----------------------------")
    print(f'Winner: {win_match}')               # printing the winner
    print("----------------------------")
    print(" ")
textfile_path=os.path.join("Analysis", "Analysis.txt")
with open(textfile_path, "w") as txt_file:
    # Writing output to the text file
    txt_file.write("Election Results\n")
    txt_file.write("-----------------------------\n")
    txt_file.write(f'Total Votes: {tot_casted_votes}\n')
    txt_file.write("-----------------------------\n")
    for i in range(len(list_cand)):
        votes_got=len([vot for vot in candidates if vot==list_cand[i]])
        perc_vot='{0:.3f}'.format(votes_got/tot_casted_votes*100)
        txt_file.write(f'{list_cand[i]}: {perc_vot}% ({votes_got})\n')
    win_match=max(winner,key=winner.get)
    txt_file.write("----------------------------\n")
    txt_file.write(f'Winner: {win_match}\n')
    txt_file.write("----------------------------")