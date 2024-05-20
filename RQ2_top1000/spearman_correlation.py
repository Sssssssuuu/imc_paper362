import pandas as pd
from scipy.stats import spearmanr

# Load the file
file_path = ''  
df = pd.read_excel(file_path)

# Assign rankings based on the index
df['ranking'] = df.index + 1

# Calculate pairwise Spearman correlation coefficients
columns = ['ranking', 'rating', 'reviews_count']
for i in range(len(columns)):
    for j in range(i + 1, len(columns)):
        col1, col2 = columns[i], columns[j]
        coef, p = spearmanr(df[col1], df[col2])
        print(f"Spearman correlation between {col1} and {col2}: coefficient={coef:.3f}, p-value={p:.3f}")
