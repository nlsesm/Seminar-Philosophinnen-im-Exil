# turtle_visualizer

This program visualizes RDF graphs from Turtle (.ttl) files as network graphs using Python. It generates an HTML file for each Turtle file and a combined HTML file for all Turtle files in a specified directory.

## Requirements
The Script will try to install the required packes themselves or you can install them manually:

- `rdflib`
- `networkx`
- `pyvis`

You can install them using pip:

```bash
pip install rdflib networkx pyvis
```

## Usage

### Folder Path

The script will automatically convert all ttl files in a given folder into graphs (+ one combined Graph). All other files will be simply ignored.
The Folder path can be either given via the first command line argument or the script can be modified by changing the path in the constant **TURTLE_FILE_FOLDER_PATH_DEFAULT** in line 26
The default location is a folder in the same directory as the script called *turtle_files*

```bash
python ttl_to_network_graph.py [folder_path]
```

### Overlap

In the Script is also a constant called **TRY_TO_AVOID_OVERLAP** which when __True__ will make the graph implement springs to try to avoid overlap of nodes. This can make the graph take longer to load and also can make it take a while to get fully stable. The default is __True__ and its recommended to leave it that way, but the option is there to set it to __False__.


### HTML Files
The HTML Files that the script outputs will be by default in the same dirctory as the script is. (make sure the script has the necessary rights there if thats non standard) 
They can be opened with any browser. Bigger files will have a loading screen before they are interactable.
The nodes in the Graph can be clicked to see all connections highlighted. The Edges in the Graph are directed and labled.
Nodes can also be moved, tho they will most likely spring back.
The naming scheme is: **\<ttl file name\>**_network_graph.hmtl