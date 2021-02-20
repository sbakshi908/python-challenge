
import os
import csv

pypoll_csv = os.path.join("Resources" ,"election_data.csv")

voter_ids = []
county = []
candidate_dict = {}

# Read in the CSV file
with open(pypoll_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)

    # Loop through the data
    for row in csvreader:
        voter_ids.append(row[0])
        county.append(row[1])
        total_votes = len(voter_ids)

        candidate_name =[]
        candidate_name = row[2]

        if candidate_name in candidate_dict:
            #tally the votes for that candidate name 
            #count = count + 1
            candidate_dict[candidate_name]+=1
        else:
            #add the new name to candidate dict and first tally 
            candidate_dict[candidate_name] = 1

    # #new for loop to get the % of each vote , create a new list for each item (name, number of votes, % of votes which can be zipped )
        num_votes = list(candidate_dict.values())
        names = list(candidate_dict.keys())
        percent_of_votes = list()
        for eachvalue in num_votes:
            percent_of_votes.append((int(eachvalue)/total_votes)*100)
            # percent_of_votes.append(eachvalue/total_votes)
#defining final variables for winner 
winner_by_votes = max(num_votes)
winner_by_percent = max(percent_of_votes)
winner_by_name = max(candidate_dict,key=candidate_dict.get)

#zip it all together
final_list = zip(names,num_votes,percent_of_votes)
final_final_list = list(final_list)
print(final_final_list)


print(f'Election Results')
print(f'-------------------')
print(f'Total Votes: {total_votes}')
print(f'-------------------------')
print(*final_final_list, sep = "\n")
print(f'-------------------------')
print(f'Winner: {winner_by_name} ')

#write to txt file 
write_only = os.path.join("Analysis", "PyPoll_Results.txt") 
with open(write_only, "w") as PyPoll_txt:
    PyPoll_txt.write(f'Election Results\n')
    PyPoll_txt.write(f'------------------\n')
    PyPoll_txt.write(f'Total Votes: {total_votes} \n')
    PyPoll_txt.write(f'-----------------------\n')
    PyPoll_txt.write(f'{final_final_list} \n')
    PyPoll_txt.write(f'Winner: {winner_by_name}')
    PyPoll_txt.close()

        

    