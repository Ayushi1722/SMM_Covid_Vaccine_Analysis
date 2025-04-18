# SMM_Covid_Vaccine_Analysis - Twitter Vaccine Sentiment

This project analyzes Twitter data related to vaccine sentiment (pro-vaccine and anti-vaccine). It collects tweets using the Twitter API, processes the data, and generates visualizations showing network graphs and statistical analysis.

## Features
- Twitter data collection via Twitter API
- Network graph analysis of tweet interactions
- Visualization of degree distribution, clustering coefficients, and centrality measures
- CSV and JSON data export

## Setup
1. Install required dependencies: `pip install -r requirements.txt`
2. Configure your Twitter API credentials in the config file
3. Run the analysis: `python run.py`

## Project Structure
- `src/`: Source code
- `data/`: Crawled and processed data
- `figures/`: Generated visualizations
- `report/`: Analysis reports and findings