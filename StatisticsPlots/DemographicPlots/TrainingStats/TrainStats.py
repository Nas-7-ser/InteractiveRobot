import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Set the style for seaborn plots
sns.set(style="whitegrid")


"""# Path to the file listing the matched CSV filenames
matched_files_path = '/Users/hann/Desktop/Developer/InteractiveRobot/StatisticsPlots/DemographicPlots/TrainingStats/matched_files.txt'

# Output directory for the plots
output_directory = '/Users/hann/Desktop/Developer/InteractiveRobot/StatisticsPlots/DemographicPlots/TrainingStats/TrainingStatsPlots'
"""
#testing the new partition to compare the plots
matched_files_path = '/Users/hann/Desktop/Developer/InteractiveRobot/StatisticsPlots/DemographicPlots/TrainingStats/TrainingStatsPlots/NewTrainingSet/matched_files.txt'
output_directory = '/Users/hann/Desktop/Developer/InteractiveRobot/StatisticsPlots/DemographicPlots/TrainingStats/TrainingStatsPlots/NewTrainingSet'


os.makedirs(output_directory, exist_ok=True)

# Demographic variables to analyze
demographic_variables = ['sex', 'politics', 'race', 'edu', 'employ', 'age']

# Initialize an empty list to store DataFrames
dfs = []

# Read the list of matched files and load their data
with open(matched_files_path, 'r') as matched_files:
    for line in matched_files:
        # Extract the file path from each line (adjust this as needed based on the format of matched_files.txt)
        line = line.strip()
        if os.path.isfile(line):
            df = pd.read_csv(line)
            # Only keep the demographic variables if they exist in the CSV
            df = df[demographic_variables].dropna(axis=1, how='all')
            dfs.append(df)

"""# Concatenate all DataFrames into a single DataFrame
combined_df = pd.concat(dfs, ignore_index=True)

# Now you can calculate and plot statistics for the combined data
for variable in combined_df.columns:
    plt.figure(figsize=(26, 10))
    if combined_df[variable].dtype == 'object' or combined_df[variable].dtype == 'category':
        # Categorical data: Plot a bar chart with seaborn
        sns.countplot(data=combined_df, x=variable, palette='viridis')
        plt.title(f'Distribution of {variable.capitalize()} (Combined Data)')
        plt.xlabel(variable.capitalize())
        plt.ylabel('Frequency')
    else:
        # Numeric data: Plot a histogram with seaborn
        sns.histplot(data=combined_df, x=variable, kde=True, color='skyblue')
        plt.title(f'Distribution of {variable.capitalize()} (Combined Data)')
        plt.xlabel(variable.capitalize())
        plt.ylabel('Density')

    # Detailed legend and labels
    plt.legend(title=variable.capitalize(), title_fontsize='13', fontsize='12', loc='best')

    # Save the plot to the specified output directory
    plot_path = os.path.join(output_directory, f'{variable}_distribution_combined_data.png')
    plt.savefig(plot_path)
    plt.close()
    print(f'Saved plot to {plot_path}')
"""

# Concatenate all DataFrames into a single DataFrame
combined_df = pd.concat(dfs, ignore_index=True)

# Calculate and plot statistics for the combined data
for variable in combined_df.columns:
    plt.figure(figsize=(26, 10))
    if combined_df[variable].dtype == 'object' or combined_df[variable].dtype == 'category':
        # Categorical data: Plot a bar chart with seaborn
        sns.countplot(data=combined_df, x=variable)
        plt.title(f'Distribution of {variable.capitalize()} (Combined Data)')
        plt.xlabel(variable.capitalize())
        plt.ylabel('Frequency')
    else:
        # Numeric data: Plot a histogram with seaborn
        sns.histplot(data=combined_df, x=variable, kde=True, color='skyblue')
        plt.title(f'Distribution of {variable.capitalize()} (Combined Data)')
        plt.xlabel(variable.capitalize())
        plt.ylabel('Density')

    # Remove the plt.legend() line to avoid the "No artists found" note
    # Save the plot to the specified output directory
    plot_path = os.path.join(output_directory, f'{variable}_distribution_combined_data.png')
    plt.savefig(plot_path)
    plt.close()
    print(f'Saved plot to {plot_path}')