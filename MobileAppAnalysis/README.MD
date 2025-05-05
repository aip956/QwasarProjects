# Welcome to My Mobapp

## Task
The mission is to analyze the Android mobile app market using the "Google Play Store Apps" dataset from Kaggle. This analysis will guide a hypothetical internal decision-making for launching a new mobile app in the Google Play Store.
- Load and clean the dataset
- Analyze app popularity, category-wise trends, pricing, and downloads
- Provide visual insights through plots (histograms, bar charts, pie charts, etc.)
- Write and publish a scientific-style blog post summarizing the findings
- Present the notebook to the hypothetical VP of Marketing and VP of Design

## Description
This project explores key metrics from the Google Play Store:
- Market size (total downloads and revenue potential)
- Category-specific trends (average installs, price, app count)
- Top paid apps in the "Family" category
- Genre distribution and pricing trends
The analysis is driven by data wrangling, statistical exploration, and visual storytelling using Python (Pandas, Matplotlib, Seaborn). It aims to help product, marketing, and design teams make informed decisions about which app category to target next.

## Installation
1. Clone this repo and change into the directory:
   ```
    git clone 
   ```

   ```
    cd
   ```
2. Set up a Python virtual environment
   ```
    python2 -m venv env
    source env/bin/activate #On Windows: .\env\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Download the dataset from Kaggle:
   1. https://www.kaggle.com/datasets/lava18/google-play-store-apps
   2. Place it in the data/ directory

## Usage
Open the Jupyter Notebook:
    ```
    jupyter notebook my_mobapp_analysis.ipynb
    ```

Functions:
- load_dataset(): Loads the Google Play Store dataset
- clean_dataset(): Cleans and normalizes columns (e.g. price, installs)
- print_summarize_dataset(): Displays high-level summary stats
- print_histograms(): Visualizes distributions of key variables
- compute_correlations_matrix(): Plots feature correlations
- print_scatter_matrix(): Generates scatterplots to explore relationships
After analysis, check out the blog report linked 

### The Core Team
Anthea Ip
Powered by:
- Python for data processing and visualization
- Pandas, Matplotlib, Seaborn for analysis and plotting
- Jupyter Notebook for experimentation and reporting
- Me, Junior Data Scientist at My Mobapp Studio!
