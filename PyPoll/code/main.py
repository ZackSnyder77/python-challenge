import os
import csv

votes = 0
candidatevotes = {}
vote_percentage = 0
vote_counts = []
candidates = []
winner = []
winner_percentage = 0

csvpath = os.path.join('..', 'Resources', 'election_data.csv')
output_path = os.path.join('..', 'Resources', 'output.txt')

with open(csvpath, newline='') as csvfile:


    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")


    for row in csvreader:
        votes = votes + 1
        vote_counts.append(row[2])
        if row[2] not in candidates:
            candidates.append(row[2])
    
    print("Election Results")
    print("-------------------------")
    print(F"Total Votes: {votes}") 
    print("-------------------------")  

    #counts the votes for each candidate
    for candidate in candidates:
        vote_percentage = float(format((vote_counts.count(candidate)/votes)*100,'.3f'))
        print(f"{candidate}: {vote_percentage}% ({vote_counts.count(candidate)})")

        if vote_percentage > winner_percentage:
            winner_percentage = vote_percentage
            winner = candidate

    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")
