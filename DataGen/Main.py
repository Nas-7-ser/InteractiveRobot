import fm
import fm_custom


if __name__ == "__main__":
    # Define the path to the dataset file
    dataset_path = 'Data preprocessing/Dataset.dat'

    # Initialize an empty graph
    graph = {}

    # Open and read the dataset file
    with open(dataset_path, 'r') as file:
        for line in file:
            node1, node2 = line.strip().split()
            if node1 not in graph:
                graph[node1] = []
            if node2 not in graph:
                graph[node2] = []
            graph[node1].append(node2)
            graph[node2].append(node1)

    fm_custom = fm_custom.FiducciaMattheyses(graph)
    partition = fm_custom.partition_graph()
    count_partition_0, count_partition_1 = fm_custom.count_partition_elements()
    print(f"Partition 0 has {count_partition_0} elements.")
    print(f"Partition 1 has {count_partition_1} elements.")

    # Specify file paths dynamically
    # Make sure to comment this if you don't want it to get regenerated while generating the seen & unseen data
    fm_custom.count_and_print_edges_within_partitions("DataGen/train.dat", "DataGen/partition_dev_test.dat")


    
#partition on the remaining dataset 
    dataset_path = 'DataGen/partition_dev_test.dat'

    # Initialize an empty graph
    graph = {}

    # Open and read the dataset file
    with open(dataset_path, 'r') as file:
        for line in file:
            node1, node2 = line.strip().split()
            if node1 not in graph:
                graph[node1] = []
            if node2 not in graph:
                graph[node2] = []
            graph[node1].append(node2)
            graph[node2].append(node1)

    fm = fm.FiducciaMattheyses(graph)
    partition = fm.partition_graph()
    count_partition_0, count_partition_1 = fm.count_partition_elements()
    print(f"Partition 0 has {count_partition_0} elements.")
    print(f"Partition 1 has {count_partition_1} elements.")

    # Specify file paths dynamically
    #to regenerate to get unseen data comment seen data and uncomment unseen
    #files saved in seen data
    fm.count_and_print_edges_within_partitions("DataGen/dev-seen.dat", "DataGen/test-seen.dat")
    #files saved in unseen data
    #fm.count_and_print_edges_within_partitions("DataGen/dev-unseen.dat", "DataGen/test-unseen.dat")






    