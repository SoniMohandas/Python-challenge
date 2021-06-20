#import modules 
import os
import csv

# Path to the csv file is assigning to a variable
#file_path=os.path.join('Resources', 'election_data.csv')
file_path=r"C:\Users\Soni Mohandas\Documents\BootCamp\Python-challenge\PyPoll\Resources\election_data.csv"

# Open file and assigning to a variable
with open(file_path) as election_file:
    # File is reading and assigning to a variable
    file_reader=csv.reader(election_file, delimiter=",")
        
    # declaring one list variable to store candidates names as equal to the number of votes they got and 
    # and a dictionary variable to store candidate name and number of votes they got. 
    candidates=[]
    winner={}
    
    # File header is assigning to start from second row when looping through data file
    file_header=next(file_reader)
    # Looping through all the data in the dataset using for loop
    for data in file_reader:
             
        # listing of candidates to a variable who recieved votes
        candidates.append(data[2])
        
    # Finding length of candidate list which is equal to total votes casted
    tot_casted_votes=len(candidates)
    # candidates list is cleaning, ie eliminating duplicate values and storing exact candidate 
    # list in another variable
    list_cand= list(set(candidates))

    print(' ')
    print("Election Results")
    print("-----------------------------")
    print(f'Total Votes: {tot_casted_votes}')  # printing total votes casted
    print("-----------------------------")
    print("")
    
    # looping through all the candidates using for loop
    for i in range(len(list_cand)):
        # Finding total votes got by each candidate using for loop comprehension and condition   
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

        