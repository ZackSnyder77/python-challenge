import os
import csv


csvpath = os.path.join('..', 'Resources', 'election_data.csv')
output_path = os.path.join('..', 'Resources', 'output.txt')

with open(csvpath, newline='') as csvfile:


    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    