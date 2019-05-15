import os, csv, decimal

budget_csv = os.path.join("..","**pybank**","budget_data.csv")

# Open and read csv
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

# Setting the variables
    Months = 0
    TotPL = 0
    totalDiff = 0
    previousMonth = 0
    firstLoop = True
    currentDiff = 0
    maxDiff = 0
    maxDate = 0
    minDiff = 0
    minDate = 0
    # Read through each row of data after the header

    for row in csvreader:
        Months = Months + 1
        TotPL = TotPL + int(row[1])
        if firstLoop == False:
            currentDiff = previousMonth - int(row[1])
            totalDiff = totalDiff + currentDiff
        previousMonth = int(row[1])
        if currentDiff > maxDiff:
            maxDiff = currentDiff
            maxDate = row[0]
        if currentDiff < minDiff:
            minDiff = currentDiff
            minDate = row[0]
        firstLoop = False

averageDiff = totalDiff / (Months - 1)

print("Budget Aanlysis")
print("--------------------------")
print("Total Number of Months: ", Months)
print("Net Profit/Loss ${:0,.2f}".format(TotPL))
print("--------------------------")
print("Average Change: -${:0,.2f}".format(averageDiff))
print("Greatest Increase: ", maxDate, " (", "${:0,.2f}".format(maxDiff),")")
print("Greatest Decrease: ", minDate, " (", "${:0,.2f}".format(minDiff),")")
print("--------------------------")

with open("PyBank_txt", "w") as pybank:
#    PyBank_Solution = csv.writer(pybank)
    print("Budget Analysis", file=pybank)
    print("--------------------------", file=pybank)
    print("Total Number of Months: ", Months, file=pybank)
    print("Net Profit/Loss ${:0,.2f}".format(TotPL), file=pybank)
    print("--------------------------", file=pybank)
    print("Average Change: -${:0,.2f}".format(averageDiff), file=pybank)
    print("Greatest Increase: ", maxDate, " (", "${:0,.2f}".format(maxDiff),")",file=pybank)
    print("Greatest Decrease: ", minDate, " (", "${:0,.2f}".format(minDiff),")", file=pybank)
    print("--------------------------", file=pybank)
