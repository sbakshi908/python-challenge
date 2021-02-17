
import os
import csv

pypoll_csv = os.path.join("Resources" ,"election_data.csv")

voter_ids = []
county = []
candidate_name =[]
#total votes



# Read in the CSV file
with open(pypoll_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)

    # Loop through the data
    for row in csvreader:
        voter_ids.append(row[0])
        county.append(row[1])
        candidate_name.append(row[2])

    #get the unique names from candidates, also need a counter to see how many times that name appears
   
    votes_for_x = 0
    for name in range(candidate_name):
        if (candidate_name[name +1])==(candidate_name[name]):
            votes_for_x +=1
print(votes_for_x)


        

    