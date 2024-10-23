#Python Section 2
import pandas as pd
import numpy as np

def calculate_distance_matrix(filename):
    # Load the distance data
    df = pd.read_csv(filename)

    # Assuming the CSV has columns: 'from_id', 'to_id', 'distance'
    # Initialize an empty DataFrame to store distances
    ids = pd.unique(df[['from_id', 'to_id']].values.ravel('K'))
    distance_matrix = pd.DataFrame(np.zeros((len(ids), len(ids))), index=ids, columns=ids)

    # Populate the distance matrix with known distances
    for index, row in df.iterrows():
        from_id = row['from_id']
        to_id = row['to_id']
        distance = row['distance']
        
        # Set distances for both directions
        distance_matrix.at[from_id, to_id] = distance
        distance_matrix.at[to_id, from_id] = distance

    # Calculate cumulative distances for indirect routes
    for k in ids:
        for i in ids:
            for j in ids:
                # Check for shorter path through k
                if distance_matrix.at[i, j] > distance_matrix.at[i, k] + distance_matrix.at[k, j]:
                    distance_matrix.at[i, j] = distance_matrix.at[i, k] + distance_matrix.at[k, j]

    # Return the final distance matrix
    return distance_matrix

# Example usage
filename = 'dataset-2.csv'
distance_matrix = calculate_distance_matrix(filename)
print(distance_matrix)
