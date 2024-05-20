import pandas as pd
from scipy.stats import spearmanr
import matplotlib.pyplot as plt
import matplotlib

# Setting font type for PDF output
matplotlib.rcParams['pdf.fonttype'] = 42

# List of Excel file paths
files = [
    # Add file paths here
]

# Lists to store correlation results from all files
all_correlations = []
all_actual_correlations = []
file_labels = []

# Loop through the list of files and perform the same analysis for each
for file_path in files:
    df = pd.read_excel(file_path)
    df['ranking'] = 1000 - df.index + 1  # Assign rankings based on index

    # Calculate and save the actual Spearman correlation coefficient
    actual_corr, _ = spearmanr(df['ranking'], df['reviews_count'])
    all_actual_correlations.append(actual_corr)

    # Calculate correlations for different random samples
    correlations = []
    for random_state in range(15):
        df_sample = df.sample(n=30, random_state=random_state)
        df_sample_sorted = df_sample.sort_index()
        df_sample_sorted['ranking'] = 1000 - df_sample_sorted.index + 1

        # Calculate and save the correlation coefficient for this sample
        coef, _ = spearmanr(df_sample_sorted['ranking'], df_sample_sorted['reviews_count'])
        correlations.append(coef)

    all_correlations.append(correlations)
    file_labels = ["Dalle", "Education", "Lifestyle", "Other", "Productivity", "Programming", "Research", "Writing"]

# Set font sizes for plot labels and titles
plt.rc('axes', labelsize=16)    
plt.rc('axes', titlesize=18)    

# Create a boxplot to visualize correlations
plt.figure(figsize=(10, 6), facecolor='white')
boxplot_elements = plt.boxplot(all_correlations, labels=file_labels, patch_artist=True,
                               boxprops=dict(facecolor='white', color='black', linewidth=1.5),
                               whiskerprops=dict(color='black', linewidth=1.5),
                               capprops=dict(color='black', linewidth=1.5),
                               medianprops=dict(color='black', linewidth=1.5))

# Plot actual Spearman correlation coefficients for each file
for i, actual_corr in enumerate(all_actual_correlations):
    plt.scatter(i + 1, actual_corr, color='black', marker='^', s=100, zorder=3)

plt.ylabel('Spearman correlation coefficient', fontsize=18)  
plt.xlabel('Categories', fontsize=18)                     
plt.xticks(rotation=30, fontsize=14)  
plt.yticks(fontsize=14)
plt.ylim(-0.2, 1)
plt.tight_layout()  
plt.show()
