import os
import csv

monthscount = 0
months = []
total = 0
maxdelta = 0
maxdeltamonth = []
mindelta = 0
mindeltamonth = []
revenues = []
runningdeltas = []
averagedeltas = 0

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
output_path = os.path.join('..', 'Resources', 'output.txt')

with open(csvpath, newline='') as csvfile:


    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
#    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    #place the revenues in a list to calc average delta later
    #place the months in a list to help find the month with the largets and smallest deltas
    for row in csvreader:
        revenues.append(int(row[1]))
        months.append(row[0])
        monthscount = monthscount + 1
        total = total + int(row[1])

    
    #calculates the deltas from the second month to the last
    #then calculates the average of all the deltas
    for i in range(len(revenues)):
        if i >0:
            # print(deltas[i]-deltas[i-1])
            runningdeltas.append(revenues[i]-revenues[i-1])
            averagedeltas = sum(runningdeltas) / (len(revenues)-1)
    
    #computes what the max MoM delta is as well as assigns the 'maxdeltamonth' to equal that month
    #computes what the min MoM delta is as well as assigns the 'mindeltamonth' to equal that month
    for i in range(len(runningdeltas)):
        if int(runningdeltas[i]) > maxdelta:
            maxdelta = int(runningdeltas[i])
            maxdeltamonth = months[i+1]
        if int(runningdeltas[i]) < mindelta:
            mindelta = int(runningdeltas[i])
            mindeltamonth = months[i+1]


    # print statements to print out the key summary stats requested
    print(f"Total Months: {monthscount}")
    print(f"Total: ${total}")
    print(f"Average Change: ${round(averagedeltas,2)}")
    print(f"Increase in Profits: {maxdeltamonth} (${maxdelta})")
    print(f"Decrease in Profits: {mindeltamonth} (${mindelta})")

with open(output_path, 'w') as txtfile:
    txtfile.write(f"Total Months: {monthscount}\n")
    txtfile.write(f"Total: ${total}\n")
    txtfile.write(f"Average Change: ${round(averagedeltas,2)}\n")
    txtfile.write(f"Increase in Profits: {maxdeltamonth} (${maxdelta})\n")
    txtfile.write(f"Decrease in Profits: {mindeltamonth} (${mindelta})\n")
    txtfile.close()