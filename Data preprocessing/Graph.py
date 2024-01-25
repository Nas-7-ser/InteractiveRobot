
import json
import csv
import os
from collections import defaultdict


# Function to process files and build the graph
def build_graph(directory, limit=5):
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


# accessing conversation files
graph_data = build_graph('/amuhome/a20031376/PycharmProjects/InteractiveRobot/CANDOR_survey_data')

# Convert graph data to JSON string
graph_json = json.dumps(graph_data, indent=2)
print(graph_json)

