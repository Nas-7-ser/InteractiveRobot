import random


class FiducciaMattheyses:
    #the previous "kinda" balanced partition, still being used to do the partition of the rest of the nodes after the first 1000 nodes for the training set
    """def __init__(self, graph):
        self.graph = graph
        self.partition = {}  # Node: Partition (0 or 1)
        self.gain = {}
        self.boundary_nodes = set()

    def initial_partition(self):
        nodes = list(self.graph.keys())
        random.shuffle(nodes)  # Randomize the node order
        half_size = len(nodes) // 2
        for node in nodes[:half_size]:
            self.partition[node] = 0
        for node in nodes[half_size:]:
            self.partition[node] = 1"""

#a version that does the partition into two sets 1st partition with a 1000 elements and the 2nd partition with the rest of the elements
    def __init__(self, graph):
        self.graph = graph
        self.partition = {}  # Node: Partition (0 or 1)
        self.gain = {}
        self.boundary_nodes = set()

    def initial_partition(self):
        nodes = list(self.graph.keys())
        random.shuffle(nodes)  # Randomize the node order
        # Set the first 1000 nodes to partition 0
        for node in nodes[:1000]:
            self.partition[node] = 0
        # Set the rest of the nodes to partition 1
        for node in nodes[1000:]:
            self.partition[node] = 1



    def compute_initial_gain(self):
        for node in self.graph:
            self.gain[node] = 0
            for neighbor in self.graph[node]:
                if self.partition[node] != self.partition[neighbor]:
                    self.gain[node] += 1
                else:
                    self.gain[node] -= 1
            if self.gain[node] != 0:
                self.boundary_nodes.add(node)

    def update_gains(self, node_to_move):
        self.partition[node_to_move] = 1 - self.partition[node_to_move]
        for neighbor in self.graph[node_to_move]:
            if self.partition[node_to_move] == self.partition[neighbor]:
                self.gain[neighbor] -= 2
                if self.gain[neighbor] == 0:
                    self.boundary_nodes.remove(neighbor)
            else:
                self.gain[neighbor] += 2
                self.boundary_nodes.add(neighbor)

    def find_node_with_max_gain(self):
        max_gain = float('-inf')
        for node in self.boundary_nodes:
            if self.gain[node] > max_gain:
                max_gain = self.gain[node]
                max_gain_node = node
        return max_gain_node

    def partition_graph(self):
        self.initial_partition()
        self.compute_initial_gain()

        for _ in range(len(self.graph)):
            if not self.boundary_nodes:
                break
            node_to_move = self.find_node_with_max_gain()
            if self.gain[node_to_move] <= 0:
                break
            self.update_gains(node_to_move)

        return self.partition

    def count_partition_elements(self):
        # New function to count elements in each partition
        count_partition_0 = sum(1 for node in self.partition if self.partition[node] == 0)
        count_partition_1 = sum(1 for node in self.partition if self.partition[node] == 1)
        return count_partition_0, count_partition_1

    def count_and_print_edges_within_partitions(self):
        # Initialize counters and containers for the edges within each partition
        edges_partition_0 = set()
        edges_partition_1 = set()

        for node, neighbors in self.graph.items():
            for neighbor in neighbors:
                # To ensure each edge is only counted once by ordering the node identifiers
                edge = tuple(sorted([node, neighbor]))

                if self.partition[node] == self.partition[neighbor]:
                    if self.partition[node] == 0:
                        edges_partition_0.add(edge)
                    else:
                        edges_partition_1.add(edge)

        # Convert sets to lists to remove duplicates and sort for consistent output
        #print(edges_partition_0)
        #print(edges_partition_1)

        edges_partition_0 = list(edges_partition_0)
        edges_partition_1 = list(edges_partition_1)

        print(f"Partition 0 has {len(edges_partition_0)} edges: {edges_partition_0}")
        print(f"Partition 1 has {len(edges_partition_1)} edges: {edges_partition_1}")


# Define the path to the dataset file
dataset_path = 'Dataset.dat'

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

fm = FiducciaMattheyses(graph)
partition = fm.partition_graph()
# print(partition)
# counting the elements in each partition
count_partition_0, count_partition_1 = fm.count_partition_elements()
print(f"Partition 0 has {count_partition_0} elements.")
print(f"Partition 1 has {count_partition_1} elements.")


fm.count_and_print_edges_within_partitions()
