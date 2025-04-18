"""
Graph plotting and visualization utilities.
"""

import os
import matplotlib.pyplot as plt
import networkx as nx

def degree_histogram_directed(G, in_degree=False, out_degree=False):
    """
    Calculate degree histogram for a directed graph.
    
    Args:
        G: NetworkX graph
        in_degree: Whether to calculate in-degree
        out_degree: Whether to calculate out-degree
        
    Returns:
        List with degree frequencies
    """
    nodes = G.nodes()
    
    if in_degree:
        in_degree_dict = dict(G.in_degree())
        degseq = [in_degree_dict.get(k, 0) for k in nodes]
    elif out_degree:
        out_degree_dict = dict(G.out_degree())
        degseq = [out_degree_dict.get(k, 0) for k in nodes]
    else:
        degseq = [v for k, v in G.degree()]
        
    dmax = max(degseq) + 1
    freq = [0 for d in range(dmax)]
    
    for d in degseq:
        freq[d] += 1
        
    return freq

def plot_degree_distribution(graphs, titles, output_dir=None):
    """
    Plot degree distribution for graphs.
    
    Args:
        graphs: List of NetworkX graphs
        titles: List of titles for the plots
        output_dir: Directory to save plots (if None, plots are shown)
    """
    for i, graph in enumerate(graphs):
        # In-degree and out-degree frequency
        in_degree_freq = degree_histogram_directed(graph, in_degree=True)
        out_degree_freq = degree_histogram_directed(graph, out_degree=True)
        
        plt.figure(figsize=(12, 8))
        plt.plot(range(len(in_degree_freq)), in_degree_freq, "go-", label='in-degree')
        plt.plot(range(len(out_degree_freq)), out_degree_freq, "bo-", label='out-degree')
        plt.legend(loc="upper right")
        
        y_max = max(max(in_degree_freq), max(out_degree_freq))
        plt.axis([0, len(in_degree_freq), 0, y_max])
        plt.xlabel('Degree')
        plt.ylabel('Frequency')
        plt.title(f'{titles[i]} Degree Distribution')
        
        if output_dir:
            plt.savefig(os.path.join(output_dir, f"{titles[i]}_degree_distribution.png"))
        else:
            plt.show()
        plt.close()

def plot_clustering_coefficients(graphs, titles, output_dir=None):
    """
    Plot clustering coefficients for graphs.
    
    Args:
        graphs: List of NetworkX graphs
        titles: List of titles for the plots
        output_dir: Directory to save plots (if None, plots are shown)
    """
    for i, graph in enumerate(graphs):
        nodes = list(graph.nodes())
        cluster_dict = nx.clustering(graph)
        coefficients = [cluster_dict.get(k, 0) for k in nodes]
        
        plt.figure(figsize=(12, 8))
        plt.plot(range(len(nodes)), coefficients, 'go-', 
                label=f'Local clustering coefficient for {titles[i]}')
        plt.legend(loc="upper right")
        plt.axis([0, len(nodes), 0, 1])
        plt.xlabel('Nodes')
        plt.ylabel('Clustering Coefficient')
        plt.title(f'Local Clustering Coefficient for {titles[i]}')
        
        if output_dir:
            plt.savefig(os.path.join(output_dir, f"{titles[i]}_clustering.png"))
        else:
            plt.show()
        plt.close()

def plot_closeness_centrality(graphs, titles, output_dir=None):
    """
    Plot closeness centrality for graphs.
    
    Args:
        graphs: List of NetworkX graphs
        titles: List of titles for the plots
        output_dir: Directory to save plots (if None, plots are shown)
    """
    for i, graph in enumerate(graphs):
        nodes = list(graph.nodes())
        closeness_dict = nx.closeness_centrality(graph)
        closeness = [closeness_dict.get(k, 0) for k in nodes]
        
        plt.figure(figsize=(12, 8))
        plt.plot(range(len(nodes)), closeness, 'go-', 
                label=f'Closeness centrality for {titles[i]}')
        plt.legend(loc="upper right")
        plt.axis([0, len(nodes), 0, 1])
        plt.xlabel('Nodes')
        plt.ylabel('Closeness Centrality')
        plt.title(f'Closeness Centrality for {titles[i]}')
        
        if output_dir:
            plt.savefig(os.path.join(output_dir, f"{titles[i]}_closeness.png"))
        else:
            plt.show()
        plt.close()

def plot_network_graphs(graphs, titles, output_dir=None):
    """
    Plot network graphs.
    
    Args:
        graphs: List of NetworkX graphs
        titles: List of titles for the plots
        output_dir: Directory to save plots (if None, plots are shown)
    """
    for i, graph in enumerate(graphs):
        plt.figure(figsize=(20, 16), dpi=80)
        nx.draw_networkx(
            graph,
            node_size=1000,
            node_color='b',
            edge_color='g',
            width=1,
            font_size=8
        )
        plt.title(f'Directed Graph for {titles[i]}')
        
        if output_dir:
            plt.savefig(os.path.join(output_dir, f"{titles[i]}_network.png"))
        else:
            plt.show()
        plt.close()

def visualize_all(graphs, titles, output_dir=None):
    """
    Generate all visualizations for the graphs.
    
    Args:
        graphs: List of NetworkX graphs
        titles: List of titles for the plots
        output_dir: Directory to save plots (if None, plots are shown)
    """
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
        
    plot_degree_distribution(graphs, titles, output_dir)
    plot_clustering_coefficients(graphs, titles, output_dir)
    plot_closeness_centrality(graphs, titles, output_dir)
    plot_network_graphs(graphs, titles, output_dir) 