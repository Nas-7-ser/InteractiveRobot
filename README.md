# InteractiveRobot



# Graph Processing and Analysis

This part describes the process of building a graph from CSV files, converting graph data into a specific format for analysis, and counting connections per node within the graph. 

## Features

- **Graph Building**: Constructs a graph from CSV files, extracting nodes and edges based on user interactions.
- **Data Conversion**: Converts the graph data into a `.dat` file format for easy processing and analysis.
- **Connection Counting**: Counts the number of connections (edges) each node (user ID) has within the graph.

## Usage

### Building the Graph

The `build_graph` function processes CSV files within a specified directory to construct a graph. It limits the number of files processed to manage dataset size and complexity.

```python
graph_data = build_graph('/path/to/csv/files', limit=1656)
```

- **Parameters**:
  - `directory`: The directory path containing CSV files to be processed.
  - `limit`: The maximum number of files to process.

### Converting Graph to .dat File

The `graph_to_dat` function takes the graph data and writes it to a `.dat` file, with each line representing an edge in the format `source target`.

```python
graph_to_dat(graph_data, 'Dataset.dat')
```

- **Parameters**:
  - `graph_data`: The graph data returned by `build_graph`.
  - `output_file`: The filename for the output `.dat` file.

### Counting Connections

The `count_connections` function calculates the number of connections for each node within the graph, providing insights into the network's structure.

```python
connections = count_connections(graph_data)
```

- **Parameters**:
  - `graph_data`: The graph data returned by `build_graph`.

## Detailed Method Documentation

### `build_graph(directory, limit=1656)`

- **Description**: Processes CSV files to construct a graph representation. Each CSV file should contain columns for `user_id`, `partner_id`, and `convo_id`.
- **Returns**: A dictionary with two keys, `nodes` and `edges`, where `nodes` is a list of dictionaries each representing a node, and `edges` is a list of dictionaries each representing an edge.

### `graph_to_dat(graph_data, output_file)`

- **Description**: Converts graph data into a `.dat` file format, with each line representing an edge as `source target`.
- **Effects**: Creates or overwrites `output_file` with the graph's edge data.

### `count_connections(graph_data)`

- **Description**: Counts the number of connections for each node in the graph, identifying how many times each node appears as a source or target in the edge list.
- **Returns**: A dictionary where keys are node IDs and values are the count of connections for that node.

## Example Workflow

1. **Build the Graph**: Start by building the graph from CSV files located in a specific directory.

    ```python
    graph_data = build_graph('/path/to/csv/files')
    ```

2. **Convert Graph to .dat File**: Convert the built graph into a `.dat` file for further analysis or use in other applications.

    ```python
    graph_to_dat(graph_data, 'Dataset.dat')
    ```

3. **Count Connections**: Analyze the graph to understand the connection distribution among nodes.

    ```python
    connections = count_connections(graph_data)
    ```








Fidducia-Mattheyes_Test_Validation.py : 

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

**Initialization**: Create an instance of the FiducciaMattheyses class by passing a graph, where the graph is represented as a dictionary with nodes as keys and lists of adjacent nodes as values.


    ```python
    graph = {...}
    fm = FiducciaMattheyses(graph)
    ```





**Partitioning the Graph** : Invoke partition_graph to partition the graph. This method returns a dictionary indicating each node’s partition.

    ```python
    python partition = fm.partition_graph()
    ```

**Counting Partition Elements** : After partitioning, use count_partition_elements to retrieve the count of nodes in each partition.


    ```python
    count_partition_0, count_partition_1 = fm.count_partition_elements()
    ```
    
    

**Counting and Saving Edges Within Partitions** : Call count_and_print_edges_within_partitions to count edges within each partition and save them into files.

    ```python
    fm.count_and_print_edges_within_partitions()
    ```

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
    ```python
    graph = {...}
    ```

# Initialize the algorithm with your graph
    ```python
    fm = FiducciaMattheyses(graph)
    ```

# Perform the partitioning
    ```python
    partition = fm.partition_graph()
    ```

# Count the elements in each partition
    ```python
    count_partition_0, count_partition_1 = fm.count_partition_elements()
    ```

# Count and save edges within partitions
    ```python
    fm.count_and_print_edges_within_partitions()
    ```









Fidducia-Mattheyes-Custom.py :

(Custom Partitioning Version)

This version is tailored to partition the graph into two sets, with the first set containing a fixed number of 1000 elements and the second set containing the remainder. 

Feature added ;

	•	Custom Initial Partitioning: Partitions the nodes into two groups, with the first group having exactly 1000 nodes and the second group containing the rest.


Data File Specification

Files Generated

	•	TrainSet.dat: Contains edges within the first partition (0). Each line represents an edge between two nodes within this partition, formatted as node1 node2.
	•	partition_1.dat: Contains edges within the second partition (1), formatted in the same manner as TrainSet.dat. This file captures the internal connectivity of the second partition.

partition_1.dat : contains the rest of the partition thats gonna be split between the TestSet and the ValidationSet using the normal Algorithm (Fidducia-Mattheyes_Test_Validation.py)




# In short : 
The Graph.py reads the csv files and process them in order to simplify the application of the algorithm, there are two versions slightly different the first is to do the partition with preset number of nodes 1000 goes to TrainSet and the remainder (partition 1) is processed by the second randomised version of the algorithm and it saves the two partitions in TestSet and ValidationSet


# Update : Adding statistics & (seen & unseen) partitions
