# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Ames Housing dataset from a CSV file
# Make sure the CSV file is placed in the working directory
ames_df = pd.read_csv('AmesHousing.csv')

# Inspect the columns to verify
# print(ames_df.columns)

# Use correct column for Cluster Sampling ('BldgType' might not be present, so you can use another column like 'Neighborhood')
# Let's use 'Neighborhood' for clustering

# 1. Simple Random Sampling (20% sample of the dataset)
simple_random_sample = ames_df.sample(frac=0.2, random_state=1)

# 2. Stratified Sampling (20% sample from each neighborhood)
stratified_sample = ames_df.groupby('Neighborhood', group_keys=False).apply(lambda x: x.sample(frac=0.2, random_state=1))

# 3. Cluster Sampling (Dividing into clusters based on neighborhood and sampling from one cluster)
# Let's assume 'Neighborhood' for clustering
cluster_sample = ames_df[ames_df['Neighborhood'] == 'NAmes']  # Selecting one cluster (Neighborhood = NAmes)

# 4. Systematic Sampling (Selecting every 10th sample in the dataset)
systematic_sample = ames_df.iloc[::10]

# Set the figure size for visualization
plt.figure(figsize=(16, 12))
sns.set(style="whitegrid")

# Visualize the sale price distribution for each sampling technique
sampling_methods = {
    "Simple Random Sample": simple_random_sample,
    "Stratified Sample": stratified_sample,
    "Cluster Sample": cluster_sample,
    "Systematic Sample": systematic_sample,
}

# Loop through each sampling technique and plot
for i, (method, sample_data) in enumerate(sampling_methods.items(), 1):
    plt.subplot(2, 2, i)
    sns.histplot(sample_data['SalePrice'], kde=True, bins=30, color='skyblue')
    plt.title(f"{method} - Sale Price Distribution")
    plt.xlabel("Sale Price ($)")
    plt.ylabel("Frequency")

plt.tight_layout()
plt.show()


# Import required libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load the Ames Housing dataset
ames_df = pd.read_csv('AmesHousing.csv')

# Measure of central tendencies for 'SalePrice' and 'TotRms AbvGrd' (Total Rooms Above Ground)
central_tendency = {}

# For Sale Price
central_tendency['SalePrice'] = {
    'Mean': ames_df['SalePrice'].mean(),
    'Median': ames_df['SalePrice'].median(),
    'Mode': ames_df['SalePrice'].mode()[0]  # Take the first mode in case of multiple
}

# For Total Rooms Above Ground
central_tendency['TotRms AbvGrd'] = {
    'Mean': ames_df['TotRms AbvGrd'].mean(),
    'Median': ames_df['TotRms AbvGrd'].median(),
    'Mode': ames_df['TotRms AbvGrd'].mode()[0]  # Take the first mode in case of multiple
}

# Convert the dictionary to a DataFrame for better readability
central_tendency_df = pd.DataFrame(central_tendency)

# Display the central tendency measures
print("Central Tendencies for 'SalePrice' and 'TotRms AbvGrd':")
print(central_tendency_df)
