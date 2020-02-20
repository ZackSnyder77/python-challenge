import os
import csv

months = 0
total = 0
revenues = []
runningdeltas = []
averagedeltas = 0

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:


    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
#    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    #place the revenues in a string to calc average later
    for row in csvreader:
        revenues.append(int(row[1]))
        months = months + 1
        total = total + int(row[1])

    
    #calculates the deltas from the second month to the last
    #then calculates the average of all the deltas

    for i in range(len(revenues)):
        if i >0:
            # print(deltas[i]-deltas[i-1])
            runningdeltas.append(revenues[i]-revenues[i-1])
            averagedeltas = sum(runningdeltas) / (len(revenues)-1)

    # print(f"Sum: {sum(runningdeltas)}")

    # print(len(deltas))
    print(f"Total Months: {months}")
    print(f"Total: ${total}")
    print(f"Average Change: ${round(averagedeltas,2)}")



    