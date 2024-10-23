#Question 10: Unroll Distance Matrix

import pandas as pd

def unroll_distance_matrix(distance_matrix_df):
    # Create a new DataFrame to hold the unrolled data
    unrolled_data = []
    
    # Iterate through the rows and columns of the distance matrix
    for id_start in distance_matrix_df.index:
        for id_end in distance_matrix_df.columns:
            # Skip the combination where id_start is the same as id_end
            if id_start != id_end:
                distance = distance_matrix_df.at[id_start, id_end]
                unrolled_data.append((id_start, id_end, distance))
    
    # Create a DataFrame from the unrolled data
    unrolled_df = pd.DataFrame(unrolled_data, columns=['id_start', 'id_end', 'distance'])
    
    return unrolled_df

# Example usage
if __name__ == "__main__":
    # Sample distance matrix DataFrame
    distance_matrix = pd.DataFrame({
        'A': [0, 5, 10, float('inf')],
        'B': [5, 0, 2, 3],
        'C': [10, 2, 0, 1],
        'D': [float('inf'), 3, 1, 0]
    }, index=['A', 'B', 'C', 'D'])

    # Call the function and print the result
    unrolled_df = unroll_distance_matrix(distance_matrix)
    print(unrolled_df)
