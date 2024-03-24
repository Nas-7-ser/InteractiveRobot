# Define the path to your .dat file
#dat_file_path = 'TestSet.dat'
#dat_file_path = 'TrainSet.dat'
#dat_file_path = 'ValidationSet.dat'

dat_file_path = '/Users/hann/Desktop/Developer/InteractiveRobot/Data preprocessing/Dataset.dat'

# Replace 'your_file_path_here' with the actual path to your .dat file
csv_file_path = dat_file_path.replace('.dat', '.csv')

# Open the .dat file and create a .csv file for writing
with open(dat_file_path, 'r') as dat_file, open(csv_file_path, 'w') as csv_file:
    # Write the header row to the .csv file
    csv_file.write('source,target\n')
    
    # Read each line from the .dat file
    for line in dat_file:
        # Split the line into source and target based on space
        source, target = line.strip().split(' ')
        
        # Write the formatted line to the .csv file
        csv_file.write(f'{source},{target}\n')

print(f'Conversion complete. CSV file saved as: {csv_file_path}')
