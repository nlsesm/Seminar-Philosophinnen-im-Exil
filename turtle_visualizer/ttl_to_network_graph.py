# Author Miclas Greve

import os
import subprocess
import sys

# List of required packages
required_packages = ["rdflib", "networkx", "pyvis"]

def install_packages():
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            print(f"{package} not found, installing...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install_packages()

import rdflib
import networkx as nx
from pyvis.network import Network
import argparse


TURTLE_FILE_FOLDER_PATH_DEFAULT = "turtle_files/"
TRY_TO_AVOID_OVERLAP = True  # can take a while until stable

# Function to load Turtle data from a file
def load_turtle_file(path):
    file_path = path
    if file_path:
        with open(file_path, "r",encoding="utf-8") as file:
            turtle_data = file.read()
        return turtle_data
    return None

def make_graphs_from_turtle_files(folder_path):
    combined_graph = nx.DiGraph()
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.ttl'):
                file_path = os.path.join(root, file)
                nx_graph = parse_turtle_and_create_graph(load_turtle_file(f"{file_path}"))
                visualize_graph_interactive(nx_graph, name=f"{file.replace('.ttl','')}_network_graph")
                combined_graph = nx.compose(combined_graph, nx_graph)
    visualize_graph_interactive(combined_graph, name="combined_network_graph")


# Function to parse Turtle data and create a graph
def parse_turtle_and_create_graph(turtle_data):
    g = rdflib.Graph()
    g.parse(data=turtle_data, format="turtle")
    nx_graph = nx.DiGraph()

    # Iterate through the triples in the rdflib graph and add edges to the NetworkX graph
    for subj, pred, obj in g:
        nx_graph.add_edge(str(subj), str(obj), label=str(pred))

    return nx_graph

# Function to visualize the NetworkX graph using pyvis
def visualize_graph_interactive(nx_graph, name="turtle_data_network_graph"):
    net = Network(height="1080px", width="100%", directed=True)
    for node in nx_graph.nodes:
        net.add_node(node, label=node, title=node, shape="brokenImage")

    for edge in nx_graph.edges(data=True):
        net.add_edge(edge[0], edge[1], title=edge[2]['label'], label=edge[2]['label'])

    # implements moving springs into the graph that try to avoid overlap
    # can take a while until stable
    if TRY_TO_AVOID_OVERLAP:
        net.set_options("""
            var options = {
                "nodes": {
                    "size":13,
                    "font": {
                        "size": 9
                    }
                },
                "edges": {
                    "arrowStrikethrough": false,
                    "color": {
                    "inherit": true
                    },
                    "font": {
                    "size": 10,
                    "align": "top"
                    },
                    "smooth": true
                },
                "physics": {
                    "barnesHut": {
                        "centralGravity": 0.2,
                        "springLength": 100,
                        "springConstant": 0.001,
                        "damping": 0.7,
                        "avoidOverlap": 1
                    },
                "maxVelocity": 5,
                "minVelocity": 0.47,
                "solver": "barnesHut"
                }
            }
            """)
        
    # Generate and display the HTML file
    output_file = f"{name}.html"
    net.show(output_file, notebook=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process TTL files and visualize RDF graphs.")
    parser.add_argument("folder_path", nargs='?', default=TURTLE_FILE_FOLDER_PATH_DEFAULT, help="Path to the folder containing TTL files")
    args = parser.parse_args()
    make_graphs_from_turtle_files(args.folder_path)



