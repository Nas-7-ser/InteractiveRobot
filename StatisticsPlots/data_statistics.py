import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import glob
import os


#[8 rows x 208 columns] this is the nature of the csv file 208 vars with 5 of them demographs

"""# Directory containing the CSV files of the CANDOR data (we're gonna do the stats on all of them, combined to compare the stats later with the stats of different partitions)
directory = '/Users/hann/Desktop/Developer/InteractiveRobot/CANDOR_survey_data'
output_directory = '/Users/hann/Desktop/Developer/InteractiveRobot/StatisticsPlots/DemographicPlots/OriginalDataStats'
"""

#stats for training data, uncomment to redo
directory = '/Users/hann/Desktop/Developer/InteractiveRobot/CANDOR_survey_data'
output_directory = '/Users/hann/Desktop/Developer/InteractiveRobot/StatisticsPlots/DemographicPlots/OriginalDataStats'

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Pattern to match all CSV files
pattern = os.path.join(directory, '*.csv')

# Demographic variables to analyze
demographic_variables = ['sex', 'politics', 'race', 'edu', 'employ', 'age']

# Initialize an empty list to store DataFrames
dfs = []

# Iterate through all CSV files in the directory and append them to the list
for csv_file in glob.glob(pattern):
    df = pd.read_csv(csv_file)
    # Only keep the demographic variables if they exist in the CSV
    df = df[demographic_variables].dropna(axis=1, how='all')
    dfs.append(df)

# Concatenate all DataFrames into a single DataFrame
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
        plt.title(f'Distribution of {variable.capitalize()} (Combined Training Data)')
        plt.xlabel(variable.capitalize())
        plt.ylabel('Density')
    
    # Detailed legend and labels
    plt.legend(title=variable.capitalize(), title_fontsize='13', fontsize='12', loc='best')

    # Save the plot to the specified output directory
    plot_path = os.path.join(output_directory, f'{variable}_distribution_combined_data.png')
    plt.savefig(plot_path)
    plt.close()
    print(f'Saved plot to {plot_path}')

#next step check on the plots of the uncomprehensible demo vars (check the candor paper)
    #then check on the Partitions (oops they're not csv files !!!) DONE BUTTT check on the data plots the graph is really problematic
    #also same for val / test
    #then next random gen or controlled gen for different partitions with interlocutors having different convos
    #Everything kinda work somehow just organise this stuff

"""# Print unique values in 'employ'
if 'employ' in combined_df.columns:
    print(combined_df['employ'].unique())
    # Or to see counts of each category
    print(combined_df['employ'].value_counts())
else:
    print("The 'employ' column does not exist in the dataset.")"""