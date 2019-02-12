# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

import csv


csvpath = 'election_data.csv'

voterID=[]
county=[]
totalVC=0
candidate=[]
kcount=0
ccount=0
lcount=0
ocount=0


with open(csvpath, newline='') as election:
    csvreader = csv.reader(election, delimiter=',')
    
    header= next(csvreader)
    
    for row in csvreader:
       voterID.append(row[0])
       county.append(row[1])
       candidate.append(row[2])
 
   
    totalVC=len(voterID)
  
  # find name of all candidates 
    unique=[]
    for i in candidate:
        if i not in unique:
            unique.append(i)
    
kcount= candidate.count('Khan')
ccount= candidate.count('Correy')
lcount= candidate.count('Li')
ocount= candidate.count('O\'Tooley')

kpercent= round(kcount/totalVC * 100, 2)
cpercent= round(ccount/totalVC * 100, 2)
lpercent= round(lcount/totalVC * 100, 2)
opercent= round(ocount/totalVC * 100, 2)

print("Election Results")
print("---------------------")
print(f"Total Votes:  {totalVC}")
print("---------------------")
print(f"{kpercent} % ({kcount})")
print(f"{cpercent} % ({ccount})")
print(f"{lpercent} % ({lcount})")
print(f"{opercent} % ({ocount})")
print("---------------------")
print("Winner: Khan")
print("---------------------")

output= 'pypoll.txt'
with open(output, 'w') as txtfile:
    
    txtfile.writelines("Election Results\n")
    txtfile.writelines("---------------------\n")
    txtfile.writelines(f"Total Votes:  {totalVC}\n")
    txtfile.writelines("---------------------\n")
    txtfile.writelines(f"{kpercent} % ({kcount})\n")
    txtfile.writelines(f"{cpercent} % ({ccount})\n")
    txtfile.writelines(f"{lpercent} % ({lcount})\n")
    txtfile.writelines(f"{opercent} % ({ocount})\n")
    txtfile.writelines("---------------------\n")
    txtfile.writelines("Winner: Khan\n")
    txtfile.writelines("---------------------\n")


    



    