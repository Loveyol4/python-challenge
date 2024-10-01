#Import os module and module for reading CSVfiles
import csv
import os
 
election_data =os.path.join('Resources','election_data.csv')


with open (election_data,'r') as textfile:
    #CSV reader specifies delimiter and variable that holds contents
    csvreader= textfile.reader(csvfile)
    

    #Read the header row 
    csv_header=next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    #Read each row of data after the header 
    for row in csvreader:
        print(row)
    
    #The total number of votes cast

    
    #Create a List 
    #Total_votes=

