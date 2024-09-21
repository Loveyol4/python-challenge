 
import os
import csv


# Create file path across operating systems
Pybank_budget_file = os.path.join("..", "Resources", "budget_data.csv")

#Create file path for saving the output
output_folder =os.path.join("..", "Analysis")
output_file =os.path.join(output_folder, "financial_analysis.txt")


# Improved Reading using CSV module
with open(Pybank_budget_file) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #Read the first row to get the initial profit loss
    first_row =next(csvreader)
    previous_profit_losses= int(first_row[1])

    # Initialize varaiables for total months, total profit, max/min profit 
    total_months = 1
    total_profit_losses = previous_profit_losses
    profit_changes = []
    dates =[first_row[0]]
    average_change_in_profit_losses= 0
    profit_increase = 0
    profit_decrease = 0 

    
    # Loop through each row in the CSV file
    for row in csvreader:
        date = row[0]  
        profit_loss = int(row[1])  

        dates.append(date)
    # Calculate the change in profit loss for each month
        change_in_profit_lossess= int(row[1]) - previous_profit_losses
        profit_changes.append(change_in_profit_lossess)
        previous_profit_losses =int(row[1])


        # Count the total months
        total_months += 1

        #calculate the total profit_loss
        total_profit_losses += profit_loss
        
    # Calculate the average profit loss
if len(profit_changes) > 0:
    average_change_in_profit_losses = sum(profit_changes) / len(profit_changes)
  
   #Calculate the max and min profit loss
    profit_increase = max(profit_changes)
    profit_decrease = min(profit_changes)
  
  #Include the date for profit increase and decrease 
    profit_increase_date = dates[profit_changes.index(profit_increase) + 1]
    profit_decrease_date = dates[profit_changes.index(profit_decrease) + 1]

else: 
   average_change_in_profit_losses = 0
   profit_increase = 0
   profit_decrease = 0
   profit_increase_date = ""
   profit_decrease_date = ""

#Print the results
output = (
    "Financial Analysis\n"
    "-----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit_losses}\n"
    f"Average Change: ${average_change_in_profit_losses:.2f}\n"
    f"Greatest Increase in Profits: {profit_increase_date} (${profit_increase})\n"
    f"Greatest Decrease in Profits: {profit_decrease_date} (${profit_decrease})\n"
)

print(output)

with open(output_file, "w") as file:
    file.write(output)

print(f"Results have been written to: {output_file}")


  
