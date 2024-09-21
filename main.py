import csv
import os

# Create file path for reading the election data
PyPoll_data = os.path.join("..", "Resources", "election_data.csv")

# Create file path for saving the output
output_folder = os.path.join("..", "Analysis")
output_file = os.path.join(output_folder, "election_results.txt")

# Improved Reading using CSV module
with open(PyPoll_data) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Initialize variables
    total_votes = 0
    candidate_votes = {}
    winner = ""
    winner_votes = 0

    # Loop through the rows to count votes and track candidates
    for row in csvreader:
        candidate_name = row[2]
        
        # Total vote count
        total_votes += 1

        # Add candidate to the dictionary if not already present
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0
        
        # Add vote to the candidate's total
        candidate_votes[candidate_name] += 1

    # Calculate the percentage of votes
    percentage_votes = {}
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        percentage = (votes / total_votes) * 100
        percentage_votes[candidate] = percentage

        # Determine the winner
        if votes > winner_votes:
            winner = candidate
            winner_votes = votes

# Prepare the output string
output = (
    "Election Results\n"
    "-----------------\n"
    f"Total Votes: {total_votes}\n"
    "------------------\n"
)

for candidate in candidate_votes:
    output += f"{candidate}: {percentage_votes[candidate]:.2f}% ({candidate_votes[candidate]})\n"

output += (
    "------------------\n"
    f"Winner: {winner}\n"
)

# Print the results to the console
print(output)

# Write the results to a file in the output folder
with open(output_file, "w") as file:
    file.write(output)

print(f"Results have been written to: {output_file}")









