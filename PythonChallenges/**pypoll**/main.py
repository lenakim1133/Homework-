import os, csv, decimal

poll_csv = os.path.join("..","**pypoll**","election_data.csv")





  

#in order to find out the list of candidates I came up with this
Cand_list = ["Khan","Correy","Li","O'Tooley"] 
Totvote=0
C1 = 0
C2 = 0
C3 = 0
C4 = 0
# Open and read csv
with open(poll_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

     # Read the header row first 
    csv_header = next(csvfile)
    for row in csvreader:
        Totvote+= +1  
        
        #I would run this in order to get the list of candidates
        #if row[2] not in Cand_list :
            #Cand_list.append(row[2])  
            #print(Cand_list.append(row[2]))
            

           
             

        if row[2] == Cand_list[0]:
                C1+=1
        elif row[2] == Cand_list[1]:
                C2+=1
        elif row[2]==Cand_list[2]:
                C3+=1
        else:
                C4+=1

  
    
    Total_C=[C1,C2,C3,C4]



    for x in Total_C:
        if C1==max(Total_C):
          Winner = Cand_list[0]
        elif C2==max(Total_C):
         Winner =Cand_list[1]
        elif C3==max(Total_C):
         Winner =Cand_list[2]
        else:
         Winner =Cand_list[3]

print("**Election Results**")
print("--------------------------")
print("Total Vote Casted: ", "{:0,.0f}".format(Totvote))
print("--------------------------")
print("<< Candidate Totals >>")
print(Cand_list[0], ": ", "{:0,.0f}".format(C1), ":", "{0:.0%}".format(C1/Totvote))
print(Cand_list[1], ": ", "{:0,.0f}".format(C2), ":", "{0:.0%}".format(C2/Totvote))
print(Cand_list[2], ": ", "{:0,.0f}".format(C3), ":", "{0:.0%}".format(C3/Totvote))
print(Cand_list[3], ": ", "{:0,.0f}".format(C4), ":", "{0:.0%}".format(C4/Totvote))
print("--------------------------")   
print("Winner: ", Winner )
print("--------------------------")

with open("PyPoll_txt","w") as pypoll:
    print("**Election Results**", file=pypoll)
    print("--------------------------", file=pypoll)
    print("Total Vote Casted: ", "{:0,.0f}".format(Totvote), file=pypoll)
    print("--------------------------", file=pypoll)
    print("<< Candidate Totals >>", file=pypoll)
    print(Cand_list[0], ": ", "{:0,.0f}".format(C1), ":", "{0:.0%}".format(C1/Totvote), file=pypoll)
    print(Cand_list[1], ": ", "{:0,.0f}".format(C2), ":", "{0:.0%}".format(C2/Totvote), file=pypoll)
    print(Cand_list[2], ": ", "{:0,.0f}".format(C3), ":", "{0:.0%}".format(C3/Totvote), file=pypoll)
    print(Cand_list[3], ": ", "{:0,.0f}".format(C4), ":", "{0:.0%}".format(C4/Totvote), file=pypoll)
    print("--------------------------", file=pypoll)   
    print("Winner: ", Winner , file=pypoll)
    print("--------------------------", file=pypoll)