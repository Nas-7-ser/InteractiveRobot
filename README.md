# InteractiveRobot


Fidducia-Mattheyes_Test_Validation.py : (i made a mistake naming the file)

Fiduccia-Mattheyses Partitioning Algorithm Documentation

The Fiduccia-Mattheyses algorithm is a heuristic method for partitioning graphs. This Python implementation provides functionalities for initial partitioning, computing and updating gains, selecting nodes with maximum gain, performing the partitioning process, and additional features for counting and saving edges within each partition.

Features

	•	Initial Partitioning: Randomly partitions the nodes into two equal groups.
	•	Gain Calculation: Computes initial gains for all nodes based on their connections.
	•	Gain Updates: Dynamically updates gains as nodes move between partitions.
	•	Node Selection: Identifies and moves the node with the maximum gain to balance partitions.
	•	Partitioning Process: Iteratively improves partition quality based on gains.
	•	Counting Elements: Counts the number of elements in each partition after partitioning.
	•	Edge Counting and Saving: Identifies and saves edges within each partition for analysis.

Usage

Initialization

Create an instance of the FiducciaMattheyses class by passing a graph, where the graph is represented as a dictionary with nodes as keys and lists of adjacent nodes as values.

graph = {...}
fm = FiducciaMattheyses(graph)

Partitioning the Graph

Invoke partition_graph to partition the graph. This method returns a dictionary indicating each node’s partition.

partition = fm.partition_graph()

Counting Partition Elements

After partitioning, use count_partition_elements to retrieve the count of nodes in each partition.

count_partition_0, count_partition_1 = fm.count_partition_elements()

Counting and Saving Edges Within Partitions

Call count_and_print_edges_within_partitions to count edges within each partition and save them into files.

fm.count_and_print_edges_within_partitions()

Data File Specification

Files Generated

	•	TestSet.dat: Stores edges within partition 0. Each line represents an edge node1 node2.
	•	ValidationSet.dat: Stores edges within partition 1. Formatted similarly to TestSet.dat, with each line representing an edge within this partition.

Saving Process

Edges are iterated over and saved into their respective files based on their partition assignment. Each edge is formatted as node1 node2 per line.

Complete Method Documentation

__init__(self, graph)

Initializes the algorithm with a given graph.

	•	Parameters:
	•	graph: A dictionary representing the graph, where keys are node identifiers and values are lists of adjacent node identifiers.

initial_partition(self)

Randomly partitions the graph’s nodes into two roughly equal groups.

compute_initial_gain(self)

Calculates the initial gain of each node, where gain is defined by the difference in the number of edges to nodes in the opposite partition versus edges to nodes in the same partition.

update_gains(self, node_to_move)

Updates the gains of nodes affected by moving node_to_move to the opposite partition.

	•	Parameters:
	•	node_to_move: The identifier of the node to be moved.

find_node_with_max_gain(self)

Identifies the node with the highest gain among all boundary nodes.

partition_graph(self)

Performs the partitioning of the graph by iteratively moving nodes to improve partition quality.

count_partition_elements(self)

Counts the number of nodes in each partition after the partitioning process.

count_and_print_edges_within_partitions(self)

Counts and saves edges within each partition to TestSet.dat and ValidationSet.dat files, capturing the internal connectivity of each partition for further analysis.

Example

# Load or define your graph
graph = {...}

# Initialize the algorithm with your graph
fm = FiducciaMattheyses(graph)

# Perform the partitioning
partition = fm.partition_graph()

# Count the elements in each partition
count_partition_0, count_partition_1 = fm.count_partition_elements()

# Count and save edges within partitions
fm.count_and_print_edges_within_partitions()








Fidducia-Mattheyes.py :

(Custom Partitioning Version)

This version is tailored to partition the graph into two sets, with the first set containing a fixed number of 1000 elements and the second set containing the remainder. 

Feature added ;

	•	Custom Initial Partitioning: Partitions the nodes into two groups, with the first group having exactly 1000 nodes and the second group containing the rest.


Data File Specification

Files Generated

	•	TrainSet.dat: Contains edges within the first partition (0). Each line represents an edge between two nodes within this partition, formatted as node1 node2.
	•	partition_1.dat: Contains edges within the second partition (1), formatted in the same manner as TrainSet.dat. This file captures the internal connectivity of the second partition.

partition_1.dat : contains the rest of the partition thats gonna be split between the TestSet and the ValidationSet using the normal Algorithm (Fidducia-Mattheyes_Test_Validation.py)
