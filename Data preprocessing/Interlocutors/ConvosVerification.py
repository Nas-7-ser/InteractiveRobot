def parse_file(file_path):
    """Parse the file and return a dict with interlocutor IDs as keys and sets of their partners as values."""
    conversations = {}
    with open(file_path, 'r') as file:
        for line in file:
            interlocutor1, interlocutor2 = line.strip().split()
            if interlocutor1 not in conversations:
                conversations[interlocutor1] = set()
            if interlocutor2 not in conversations:
                conversations[interlocutor2] = set()
            conversations[interlocutor1].add(interlocutor2)
            conversations[interlocutor2].add(interlocutor1)
    return conversations

def compare_convos(conversations1, conversations2):
    """Compare the conversations from two sets and print new conversations for each interlocutor."""
    for interlocutor, partners1 in conversations1.items():
        partners2 = conversations2.get(interlocutor, set())
        new_conversations = partners2 - partners1
        if new_conversations:
            print(f'Interlocutor {interlocutor} had new conversations with: {new_conversations}')

# Path to your data files
file_path1 = '/Users/hann/Desktop/Developer/InteractiveRobot/Data preprocessing/TrainSet.dat'
file_path2 = '/Users/hann/Desktop/Developer/InteractiveRobot/TrainSet.dat'

# Parse the files
conversations1 = parse_file(file_path1)
conversations2 = parse_file(file_path2)

# Compare conversations from the two files
compare_convos(conversations1, conversations2)
