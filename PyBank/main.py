import csv

csvpath = 'budget_data.csv'

dates=[]
revenue=[]

with open(csvpath, newline='') as budget:
    csvreader = csv.reader(budget, delimiter=',')
    header= next(csvreader)
    data= [row for row in csvreader]

    for row in data:
        dates.append(row[0])
        revenue.append(int(row[1]))


# testing-print(header)
# testing-print(data[0])

#find total months
totalmonths= len(dates)

#find total revenue
net= sum(revenue)
# print(totalmonths)

previous= 0
greatest= 0
lowest= 0

#find greatest increase and descrease
for i in range(len(revenue)):
    
    delta= int(revenue[i])-previous
    if delta > greatest:
        greatest= delta
        mI= dates[i]
        
        
    elif delta < lowest:
        lowest=delta
        mD= dates[i]
        
    previous= int(revenue[i])

#difference between last and first profit
difference= revenue[-1]- revenue[-0]

#find average 
average= round(difference/(totalmonths-1) ,2)

#testing- print(average)    
  

#print to terminal
print("Finacial Analyis")
print("---------------------------")
print(f"Total Months: {totalmonths}")
print(f"Total: $ {net}")
print(f"Average Change: $ {average}")
print(f"Greatest Increase in Profits: {mI} ${greatest}")
print(f"Greatest Decrease in Losses: {mD} ${lowest}")

#print to text
output= 'pybank.txt'
with open(output, 'w') as txtfile:
    txtfile.writelines("Finacial Analyis \n")
    txtfile.writelines("--------------------------- \n")
    txtfile.writelines(f"Total Months: {totalmonths} \n")
    txtfile.writelines(f"Total Amount: $ {net} \n")
    txtfile.writelines(f"Greatest Increase in Profits: {mI} ${greatest} \n")
    txtfile.writelines(f"Greatest Decrease in Losses: {mD} ${lowest} \n") 

        
    