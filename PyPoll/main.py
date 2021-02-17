
import os
import csv

pypoll_csv = os.path.join("Resources" ,"election_data.csv")

voter_ids = []
county = []
candidate_dict = {}

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

        candidate_name = row[2]
        count = 0
        if candidate_name in candidate_dict:
            #tally the votes for that candidate name 
            #count = count + 1
            candidate_dict[candidate_name]+=1
        else:
            #add the new name to candidate dict and first tally 
            candidate_dict[candidate_name] = 1

print(candidate_dict)
print (len(voter_ids))

    #get the unique names from candidates, also need a counter to see how many times that name appears
   
#     votes_for_x = 0
#     for name in range(candidate_name):
#         if (candidate_name[name +1])==(candidate_name[name]):
#             votes_for_x +=1
# print(votes_for_x)


        

    