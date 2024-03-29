import json
import csv
import os
from collections import defaultdict


# Function to process files and build the graph
def build_graph(directory, limit=1656):
    nodes = set()
    edges = []
    files_processed = 0

    for filename in os.listdir(directory):
        if filename.endswith('.csv') and files_processed < limit:
            with open(os.path.join(directory, filename), 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    user_id = row.get('user_id')
                    partner_id = row.get('partner_id')
                    convo_id = row.get('convo_id')
                    if user_id and partner_id and convo_id:
                        nodes.add(user_id)
                        nodes.add(partner_id)
                        edges.append({"id": convo_id, "source": user_id, "target": partner_id})

            files_processed += 1
            if files_processed >= limit:
                break

    # Convert nodes set to list of dicts for JSON
    nodes_json = [{"id": node_id} for node_id in nodes]

    return {"nodes": nodes_json, "edges": edges}




# New function to convert graph JSON to .dat file
def graph_to_dat(graph_data, output_file):
    with open(output_file, 'w') as file:
        for edge in graph_data['edges']:
            source = edge['source']
            target = edge['target']
            file.write(f'{source} {target}\n')


# accessing conversation files
#graph_data = build_graph('/amuhome/a20031376/PycharmProjects/InteractiveRobot/CANDOR_survey_data')
graph_data = build_graph('/Users/hann/PycharmProjects/InteractiveRobot/CANDOR_survey_data')

# Convert graph data to JSON string
graph_json = json.dumps(graph_data, indent=2)
print(graph_json)

# Convert graph data to .dat file
graph_to_dat(graph_data, 'Dataset.dat')


# New function to count connections for each ID
def count_connections(graph_data):
    connection_counts = defaultdict(int)
    for edge in graph_data['edges']:
        source = edge['source']
        target = edge['target']
        connection_counts[source] += 1
        connection_counts[target] += 1
    return connection_counts


# Count connections for each ID
connections = count_connections(graph_data)
print(connections)
