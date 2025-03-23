#%%
import networkx as nx
from rdflib import Graph, Namespace, RDF
import matplotlib.pyplot as plt

#%%
bot = Namespace("https://w3id.org/bot#")
props = Namespace("http://lbd.arch.rwth-aachen.de/props#")
inst = Namespace("https://www.datathon2024.com/CHU3D#")

def load_ttl_to_networkx(ttl_file):
    rdf_graph = Graph()
    rdf_graph.parse(ttl_file, format="ttl")
    
    nx_graph = nx.Graph()
    
    for subj, obj in rdf_graph.subject_objects(bot.hasSpace):
        nx_graph.add_edge(str(subj), str(obj), label="hasSpace")
        #print(f"Added edge: {subj} - hasSpace -> {obj}")
    
    for subj, obj in rdf_graph.subject_objects(bot.hasBuilding):
        nx_graph.add_edge(str(subj), str(obj), label="hasBuilding")
        #print(f"Added edge: {subj} - hasBuilding -> {obj}")
    
    return nx_graph

def get_space_nodes(ttl_file):
    rdf_graph = Graph()
    rdf_graph.parse(ttl_file, format="ttl")
        
    space_data = []
    
    for subj in rdf_graph.subjects(RDF.type, bot.Space):
        name = rdf_graph.value(subj, props.nameIfcRoot_attribute_simple, default=None)
        longname = rdf_graph.value(subj, props.longNameIfcSpatialStructureElement_attribute_simple, default=None)
        ref_simple = rdf_graph.value(subj, props.reference_simple, default=None)
        
        space_data.append({
            "space": str(subj),
            "name": str(name) if name else None,
            "longname": str(longname) if longname else None,
            "reference_simple": str(ref_simple) if ref_simple else None
        })
    
    return space_data

def find_path(nx_graph, start_node, end_node):
    if nx.has_path(nx_graph, start_node, end_node):
        path = nx.shortest_path(nx_graph, source=start_node, target=end_node)
        return path
    else:
        return None


#%%
# Example usage
ttl_file = "./resources/050_BOCAGE CENTRAL_FC_PROJET_20 02 2024_LBD.ttl"

nx_graph = load_ttl_to_networkx(ttl_file)

#%%
start_node = "https://www.datathon2024.com/CHU3D#space_a74ac6e4-5b4b-466b-a8d0-d49db6898684"
end_node = "https://www.datathon2024.com/CHU3D#space_a74ac6e4-5b4b-466b-a8d0-d49db6898671"
path = find_path(nx_graph, start_node, end_node)
print(f"Path from {start_node} to {end_node}:", path)

#space_nodes = get_space_nodes(ttl_file)

#print("Nodes:", nx_graph.nodes())
#print("Edges:", nx_graph.edges(data=True))
#print("Space Nodes:", space_nodes)


# %%
# to import in neo4j
# add neosemantics plugin

# create the constraints and the graph config
# CREATE CONSTRAINT n10s_unique_uri FOR (r:Resource) REQUIRE r.uri IS UNIQUE
# CALL n10s.graphconfig.init({handleVocabUris: 'MAP'})

# import the graph
# CALL n10s.rdf.import.fetch("file:///G:\\dev\\datathon2024\\resources\\050_BOCAGE CENTRAL_FC_PROJET_20 02 2024_LBD.ttl", "Turtle");

# remove unused nodes (wall, slab, etc)
# MATCH (n:Element) DETACH DELETE n;

# find the shortest path between two spaces
# MATCH (start {nameIfcRoot_attribute_simple: "BCN.W.02.031"}), (end {nameIfcRoot_attribute_simple: "BCN.E.02.037A"}), 
#      p = shortestPath((start)-[*]-(end))
# RETURN p;

