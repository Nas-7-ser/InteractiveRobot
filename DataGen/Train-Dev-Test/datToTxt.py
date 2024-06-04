import glob
import pandas as pd

# Paths for data and output 

csv_directory = '/Users/hann/Desktop/Developer/InteractiveRobot/CANDOR_survey_data/*.csv'

# for train.dat
dat_file_path = '/Users/hann/Desktop/Developer/InteractiveRobot/DataGen/train.dat'
convo_id_output_path = '/Users/hann/Desktop/Developer/InteractiveRobot/DataGen/Train-Dev-Test/train.txt'

"""# for dev-seen.dat
dat_file_path = '/Users/hann/Desktop/Developer/InteractiveRobot/DataGen/dev-seen.dat'
convo_id_output_path = '/Users/hann/Desktop/Developer/InteractiveRobot/DataGen/Train-Dev-Test/dev-seen.txt'
"""
"""# for dev-unseen.dat
dat_file_path = '/Users/hann/Desktop/Developer/InteractiveRobot/DataGen/dev-unseen.dat'
convo_id_output_path = '/Users/hann/Desktop/Developer/InteractiveRobot/DataGen/Train-Dev-Test/dev-unseen.txt'

"""

"""# for test-seen.dat
dat_file_path = '/Users/hann/Desktop/Developer/InteractiveRobot/DataGen/test-seen.dat'
convo_id_output_path = '/Users/hann/Desktop/Developer/InteractiveRobot/DataGen/Train-Dev-Test/test-seen.txt'
"""

"""# for test-unseen.dat
dat_file_path = '/Users/hann/Desktop/Developer/InteractiveRobot/DataGen/test-unseen.dat'
convo_id_output_path = '/Users/hann/Desktop/Developer/InteractiveRobot/DataGen/Train-Dev-Test/test-unseen.txt'
"""


# Read the .dat file and store ID pairs
id_pairs = []
with open(dat_file_path, 'r') as dat_file:
    for line in dat_file:
        id_pairs.append(line.strip().split())

# Initialize a set to collect all unique convo_ids
convo_ids = set()

# Search all CSV files for matching ID pairs
for csv_file in glob.glob(csv_directory):
    df = pd.read_csv(csv_file)

    # Check each ID pair in the current CSV
    for id_pair in id_pairs:
        user_id, partner_id = id_pair
        
        # Find rows where user_id and partner_id match the current ID pair
        match = df[((df['user_id'] == user_id) & (df['partner_id'] == partner_id)) |
                   ((df['user_id'] == partner_id) & (df['partner_id'] == user_id))]
        
        # If a match is found, add the convo_ids to the set
        if not match.empty:
            convo_ids.update(match['convo_id'].astype(str).tolist())  # Convert to string if not already

# Save the collected convo_ids to a file
with open(convo_id_output_path, 'w') as output_file:
    for convo_id in sorted(convo_ids):  # Optional sorting for easier reading
        output_file.write(f"{convo_id}\n")

print(f"Conversation IDs saved to {convo_id_output_path}")
