import glob
import pandas as pd


# Path to the .dat file
#previous one 
#dat_file_path = '/Users/hann/Desktop/Developer/InteractiveRobot/Data preprocessing/TrainSet.dat'
#new one for comparison
dat_file_path = '/Users/hann/Desktop/Developer/InteractiveRobot/TrainSet.dat'

# Directory containing the CSV files
csv_directory = '/Users/hann/Desktop/Developer/InteractiveRobot/CANDOR_survey_data/*.csv'

#saving the matched CSV file names
output_file_path = '/Users/hann/Desktop/Developer/InteractiveRobot/StatisticsPlots/DemographicPlots/TrainingStats/TrainingStatsPlots/NewTrainingSet/matched_files.txt'

"""# Read the .dat file and store ID pairs
id_pairs = []
with open(dat_file_path, 'r') as dat_file:
    for line in dat_file:
        id_pairs.append(line.strip().split())

# Function to search all CSV files for matching ID pairs
def search_csv_files(id_pairs, csv_directory):
    matches = {}  # Dictionary to store matches: {ID pair: CSV file}

    # Iterate through each CSV file
    for csv_file in glob.glob(csv_directory):
        df = pd.read_csv(csv_file)
        
        # Check each ID pair in the current CSV
        for id_pair in id_pairs:
            user_id, partner_id = id_pair
            
            # Find rows where user_id and partner_id match the current ID pair
            match = df[((df['user_id'] == user_id) & (df['partner_id'] == partner_id)) |
                       ((df['user_id'] == partner_id) & (df['partner_id'] == user_id))]
            
            # If a match is found, store the CSV file path
            if not match.empty:
                matches[tuple(id_pair)] = csv_file
                break  # Assuming only one match is needed per ID pair

    return matches

# Search for matches
matches = search_csv_files(id_pairs, csv_directory)

# Print the matches
for id_pair, csv_file in matches.items():
    print(f"Match for ID pair {id_pair}: {csv_file}")


# Read the .dat file and store ID pairs
id_pairs = []
with open(dat_file_path, 'r') as dat_file:
    for line in dat_file:
        id_pairs.append(line.strip().split())

# Initialize a dictionary to store matches: {ID pair: [CSV files]}
matches = {tuple(id_pair): [] for id_pair in id_pairs}

# Search all CSV files for matching ID pairs
for csv_file in glob.glob(csv_directory):
    df = pd.read_csv(csv_file)
    
    # Check each ID pair in the current CSV
    for id_pair in id_pairs:
        user_id, partner_id = id_pair
        
        # Find rows where user_id and partner_id match the current ID pair
        match = df[((df['user_id'] == user_id) & (df['partner_id'] == partner_id)) |
                   ((df['user_id'] == partner_id) & (df['partner_id'] == user_id))]
        
        # If a match is found, append the CSV file path to the matches dictionary
        if not match.empty:
            matches[tuple(id_pair)].append(csv_file)

# Save the matched file names to a file
with open(output_file_path, 'w') as output_file:
    for id_pair, files in matches.items():
        if files:  # Only save if there are matched files for this ID pair
            output_file.write(f"ID Pair {id_pair}: \n")
            for file in files:
                output_file.write(f"{file}\n")
            output_file.write("\n")

print(f"Matched file names saved to {output_file_path}")

# 7 min execution time lol"""


# Read the .dat file and store ID pairs
id_pairs = []
with open(dat_file_path, 'r') as dat_file:
    for line in dat_file:
        id_pairs.append(line.strip().split())

# Initialize a dictionary to store matches: {ID pair: [CSV files]}
matches = {tuple(id_pair): [] for id_pair in id_pairs}

# Search all CSV files for matching ID pairs
for csv_file in glob.glob(csv_directory):
    df = pd.read_csv(csv_file)
    
    # Check each ID pair in the current CSV
    for id_pair in id_pairs:
        user_id, partner_id = id_pair
        
        # Find rows where user_id and partner_id match the current ID pair
        match = df[((df['user_id'] == user_id) & (df['partner_id'] == partner_id)) |
                   ((df['user_id'] == partner_id) & (df['partner_id'] == user_id))]
        
        # If a match is found, append the CSV file path to the matches dictionary
        if not match.empty:
            matches[tuple(id_pair)].append(csv_file)

# Save the matched file names to a file
with open(output_file_path, 'w') as output_file:
    for id_pair, files in matches.items():
        if files:  # Only write if there are matched files for this ID pair
            output_file.write(f"ID Pair {id_pair}: \n")
            for file in files:
                output_file.write(f"{file}\n")
            output_file.write("\n")

# Calculate and print the summary of matched and unmatched ID pairs
matched_pairs_count = sum(1 for files in matches.values() if files)
unmatched_pairs_count = len(id_pairs) - matched_pairs_count

print(f"Matched ID pairs: {matched_pairs_count} / {len(id_pairs)}")
print(f"Unmatched ID pairs: {unmatched_pairs_count}")

# Make sure the summary also gets written to the output file
with open(output_file_path, 'a') as output_file:
    output_file.write(f"\nMatched ID pairs: {matched_pairs_count} / {len(id_pairs)}\n")
    output_file.write(f"Unmatched ID pairs: {unmatched_pairs_count}\n")

print(f"Matched file names and summary saved to {output_file_path}")