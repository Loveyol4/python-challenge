import os
import csv

#Path to collect data from the Resources folder
budget_file = os.path.join('Resources','budget_data.csv')

#Define the sum of "budget_data" and "Pybank_budget" is the sole parameter 

def total_budget(Pybank_budget):

    Date = (Pybank_budget [0])
    Profit_losses = (Pybank_budget [1])

    #Total number of months in Pybank_budget 
Total_months = len(Date) # Is there a reason why Date is showing an error 86

#The total amount of "Profit/Losses"

Total_Profit= sum(Profit_losses) #Is there a reason why Profit_losses is showing an error $22564198

#this will be the sum of the losses (-) and the average- losses/profit (totals) $-8311.11 (1111.11)
Change_in_Profit = 

# I will use the max function to find the greatest increase in Profits ($1862002)
Max_Profit = 

 # I will use the min  function to find the greatet decrease in Profits $-1825558
Min_Profit = 

#Read in the csv file 
with open(budget_file, 'r') as csvfile:
    #Split the data on commas
    csvreader = csv.reader(csvfile, delimiter = ',')
    print(csvreader)

# Read and print headers and rows

    header = next(csvreader) 
    print(f"header; {header}")
    for row in csvreader:
        #print(row)

#Define the sum of the "budget_data" and "Pybank_budget" is the sole parameter 
           
          #  def total_budget(Pybank_budget):
           #     Date = (Pybank_budget [0])
            #    Profit_losses = (Pybank_budget [1])

#Total number of months of Pybank_budget
             #   Total_months = len(Date)
              #  print(Total_months)



    

    

                           