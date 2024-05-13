def read_dataset(file_path):
    # Initialize a set to hold the conversation pairs
    dataset = set()
    try:
        # Open the file and read line by line
        with open(file_path, 'r') as file:
            for line in file:
                # Assume each line contains a pair of IDs separated by a space
                pair = tuple(line.strip().split())
                if len(pair) == 2:  # Ensure the line correctly contains two elements
                    dataset.add(pair)
    except Exception as e:
        print(f"Failed to read from {file_path}: {e}")
    return dataset

# Paths to the dataset files
file_path_1 = 'DataGen/dev-unseen.dat'
file_path_2 = 'DataGen/test-unseen.dat'

# Read datasets
dataset_1 = read_dataset(file_path_1)
dataset_2 = read_dataset(file_path_2)

# Find common conversations
common_conversations = dataset_1.intersection(dataset_2)

# Display the result
print("Common Conversations:")
for conversation in common_conversations:
    print(conversation)

# Check if the two datasets have the exact same conversations
if dataset_1 == dataset_2:
    print("Both datasets have exactly the same conversations.")
else:
    print("The datasets do not have the same conversations.")
