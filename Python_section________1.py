#Question 8: Time Check

import pandas as pd

def check_timestamp_completeness(df):
    # Combine date and time columns into a single datetime column
    df['start_datetime'] = pd.to_datetime(df['startDay'] + ' ' + df['startTime'])
    df['end_datetime'] = pd.to_datetime(df['endDay'] + ' ' + df['endTime'])

    # Set multi-index for easier grouping
    df.set_index(['id', 'id_2'], inplace=True)

    # Function to check if a (id, id_2) pair has complete timestamps
    def check_pair(group):
        # Check the full range of timestamps
        start_min = group['start_datetime'].min()
        end_max = group['end_datetime'].max()

        # Check for the 24-hour period (same day check)
        full_day = (end_max - start_min).days == 0 and (end_max - start_min).seconds == 86400

        # Get unique days covered
        unique_days = group['start_datetime'].dt.dayofweek.unique()
        
        # Check if all 7 days are covered
        full_week = len(unique_days) == 7

        # Return True if either condition fails
        return not (full_day and full_week)

    # Apply the function to each group and return the results
    result = df.groupby(level=[0, 1]).apply(check_pair)
    
    return result

# Example usage
# Load the dataset
df = pd.read_csv('dataset-1.csv')
# Check the completeness of timestamps
result = check_timestamp_completeness(df)
print(result)
