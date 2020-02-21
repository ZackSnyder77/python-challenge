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
output_path = os.path.join('..', 'Resources', 'results.txt')

with open(csvpath, newline='') as csvfile:


    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)
    
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # tallies the total votes in the dataset
    #places the candidate votes into a list
    #places unique candidates into a list
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
        print(f"{candidate}: {format(vote_percentage,'.3f')}% ({vote_counts.count(candidate)})")

        if vote_percentage > winner_percentage:
            winner_percentage = vote_percentage
            winner = candidate

    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")
    
    #takes the console output and places them into a 'Results' txt file
    with open(output_path, 'w') as txtfile:
        txtfile.write("-------------------------\n")
        txtfile.write(F"Total Votes: {votes}\n") 
        txtfile.write("-------------------------\n")
        for candidate in candidates: 
            vote_percentage = float(format((vote_counts.count(candidate)/votes)*100,'.3f'))
            txtfile.write(f"{candidate}: {format(vote_percentage,'.3f')}% ({vote_counts.count(candidate)})\n")
        txtfile.write("-------------------------\n")
        txtfile.write(f"Winner: {winner}\n")
        txtfile.write("-------------------------\n")
        txtfile.close()