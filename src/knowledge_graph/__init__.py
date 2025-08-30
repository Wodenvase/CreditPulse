import networkx as nx
import streamlit as st

def build_relationships(bond_data):
    """
    Build a knowledge graph from bond data.
    Expects bond_data as a dict with keys: issuer, sector, rating, bond_id.
    """
    G = nx.DiGraph()
    issuer = bond_data.get("issuer", "Unknown Issuer")
    sector = bond_data.get("sector", "Unknown Sector")
    rating = bond_data.get("rating", "Unknown Rating")
    bond_id = bond_data.get("bond_id", "Unknown Bond")

    # Add nodes and edges
    G.add_edge(issuer, sector, relation="belongs_to_sector")
    G.add_edge(issuer, rating, relation="has_rating")
    G.add_edge(issuer, bond_id, relation="issues_bond")

    return G

def visualize_knowledge_graph(G):
    """
    Visualize the knowledge graph using Streamlit.
    """
    import matplotlib.pyplot as plt

    plt.figure(figsize=(6, 4))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10)
    st.pyplot(plt)
    plt.clf()

def contagion_path(G, from_issuer, to_issuer):
    """
    Find contagion path between two issuers (if any).
    """
    try:
        path = nx.shortest_path(G, source=from_issuer, target=to_issuer)
        return path
    except nx.NetworkXNoPath:
        return None