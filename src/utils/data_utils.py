"""
Data utilities for processing and converting data.
"""

import os
import csv
import json
import networkx as nx

def convert_to_json(csv_file, json_file):
    """
    Convert CSV file to JSON format.
    
    Args:
        csv_file: Path to CSV file
        json_file: Path to output JSON file
    """
    res = {}
    with open(csv_file, encoding='utf-8') as csvf:
        csv_reader = csv.DictReader(csvf)
        for rows in csv_reader:
            res[rows['username']] = rows
    
    with open(json_file, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(res, indent=4))

def generate_graph(df):
    """
    Generate a directed graph from Twitter data.
    
    The directed graph is implemented as follows:
    - If A mentions B in A's tweet: A->B edge will be present
    - If A retweets B's Tweet: A->B edge will be present
    
    Args:
        df: DataFrame containing tweet data
        
    Returns:
        NetworkX DiGraph object
    """
    DG = nx.DiGraph()
    
    for _, row in df.iterrows():
        # Add edges for mentions
        if row['user_mention']:
            for x in row['user_mention']:
                if x != row['username'] and not DG.has_edge(row['username'], x):
                    DG.add_edge(row['username'], x)
        else:
            DG.add_node(row['username'])
        
        # Add edges for retweets
        if row['retweetScreenNames'] != '' and row['retweetScreenNames'] != row['username']:
            DG.add_edge(row['username'], row['retweetScreenNames'])
    
    return DG

def save_data_files(dataframes, file_prefixes, output_dir):
    """
    Save dataframes as CSV and JSON files.
    
    Args:
        dataframes: List of pandas DataFrames
        file_prefixes: List of prefixes for output files
        output_dir: Directory to save files in
    """
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    for i, df in enumerate(dataframes):
        csv_path = os.path.join(output_dir, f"{file_prefixes[i]}.csv")
        json_path = os.path.join(output_dir, f"{file_prefixes[i]}.json")
        
        # Save as CSV
        df.to_csv(csv_path, index=False)
        
        # Convert to JSON
        convert_to_json(csv_path, json_path) 