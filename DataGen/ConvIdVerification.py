import os

def read_dataset(file_path):
    # Initialize a set to hold the conversation IDs
    dataset = set()
    try:
        # Open the file and read line by line
        with open(file_path, 'r') as file:
            for line in file:
                conversation_id = line.strip()
                if conversation_id:  # Ensure the line is not empty
                    dataset.add(conversation_id)
    except Exception as e:
        print(f"Failed to read from {file_path}: {e}")
    return dataset

def write_dataset(file_path, dataset):
    try:
        # Open the file and write line by line
        with open(file_path, 'w') as file:
            for conversation_id in dataset:
                file.write(f"{conversation_id}\n")
    except Exception as e:
        print(f"Failed to write to {file_path}: {e}")




def make_datasets_disjoint(file_list):
    datasets = {}
    
    # Read datasets from files
    for file_path in file_list:
        datasets[file_path] = read_dataset(file_path)
    
    # Track used conversation IDs
    used_conversations = set()
    
    # Modify datasets to remove common conversations
    for file_path in file_list:
        original_dataset = datasets[file_path]
        unique_dataset = original_dataset - used_conversations
        datasets[file_path] = unique_dataset
        used_conversations.update(unique_dataset)
    
    # Write the modified datasets back to files
    for file_path, dataset in datasets.items():
        write_dataset(file_path, dataset)
    
    print("Datasets have been verified and modified to ensure no overlap.")

# Example usage
file_list = [
    'DataGen/Train-Dev-Test/train.txt',
    'DataGen/Train-Dev-Test/dev-seen.txt',
    'DataGen/Train-Dev-Test/dev-unseen.txt', 
    'DataGen/Train-Dev-Test/test-seen.txt',
    'DataGen/Train-Dev-Test/test-unseen.txt'
]

make_datasets_disjoint(file_list)