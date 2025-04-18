"""
Main entry point for the Social Media Analysis project.
"""

import os
import argparse
import matplotlib.pyplot as plt
from .config import (
    PRO_VACCINE_HASHTAGS,
    ANTI_VACCINE_HASHTAGS,
    DEFAULT_TWEET_COUNT,
    DEFAULT_START_DATE,
    DATA_DIR,
    FIGURES_DIR
)
from .data_processing.twitter_crawler import (
    get_twitter_api,
    crawl_twitter,
    form_query
)
from .utils.data_utils import (
    generate_graph,
    save_data_files
)
from .visualization.plot_graphs import visualize_all

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Social Media Analysis Tool')
    parser.add_argument(
        '--num-tweets', 
        type=int, 
        default=DEFAULT_TWEET_COUNT,
        help='Number of tweets to retrieve'
    )
    parser.add_argument(
        '--start-date', 
        type=str, 
        default=DEFAULT_START_DATE,
        help='Start date for tweet retrieval (YYYY-MM-DD)'
    )
    parser.add_argument(
        '--interactive', 
        action='store_true',
        help='Run in interactive mode'
    )
    return parser.parse_args()

def get_start_date_interactive():
    """Get start date interactively from the user."""
    print("FDA granted Covid vaccine from December 11, 2020.")
    print("Do you need tweets from the same date onwards? (Y/N)")
    
    ans = input().strip().lower()
    
    if ans == 'y':
        return DEFAULT_START_DATE
    else:
        print("Enter the date from which tweets are required (YYYY-MM-DD):")
        return input().strip()

def main():
    """Main function to run the analysis."""
    # Parse arguments
    args = parse_arguments()
    
    # Determine start date
    date_since = args.start_date
    if args.interactive:
        date_since = get_start_date_interactive()
    
    # Create output directories
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(FIGURES_DIR, exist_ok=True)
    
    # Define queries
    queries = [PRO_VACCINE_HASHTAGS, ANTI_VACCINE_HASHTAGS]
    file_prefixes = ['proVaccineTweets', 'antiVaccineTweets']
    titles = ['Pro Vaccine', 'Anti Vaccine']
    
    # Get Twitter API
    api = get_twitter_api()
    
    # Process each query
    dataframes = []
    graphs = []
    
    for i, hashtags in enumerate(queries):
        # Create query
        query = form_query(hashtags)
        
        # Crawl Twitter
        print(f"Crawling Twitter for {titles[i]} tweets...")
        df = crawl_twitter(query, date_since, args.num_tweets, api)
        dataframes.append(df)
        
        # Generate graph
        print(f"Generating graph for {titles[i]} tweets...")
        graph = generate_graph(df)
        graphs.append(graph)
    
    # Save data files
    print("Saving data files...")
    save_data_files(dataframes, file_prefixes, DATA_DIR)
    
    # Visualize results
    print("Generating visualizations...")
    visualize_all(graphs, titles, FIGURES_DIR)
    
    print("Analysis complete!")
    print(f"Data saved to: {os.path.abspath(DATA_DIR)}")
    print(f"Figures saved to: {os.path.abspath(FIGURES_DIR)}")

if __name__ == '__main__':
    main() 