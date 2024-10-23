#Question 11: Finding IDs within Percentage Threshold

import pandas as pd

def calculate_toll_rate(df):
    # Define the rate coefficients for each vehicle type
    rates = {
        'moto': 0.8,
        'car': 1.2,
        'rv': 1.5,
        'bus': 2.2,
        'truck': 3.6
    }
    
    # Calculate toll rates for each vehicle type and add to the DataFrame
    for vehicle, rate in rates.items():
        df[vehicle] = df['distance'] * rate  # Calculate the toll rate for each vehicle type

    return df

# Example usage
if __name__ == "__main__":
    # Sample DataFrame based on Question 10 (with id_start, id_end, and distance)
    data = {
        'id_start': ['A', 'A', 'B', 'B', 'C', 'D'],
        'id_end': ['B', 'C', 'A', 'D', 'D', 'A'],
        'distance': [5, 8, 5, 7, 10, 6]
    }
    
    df = pd.DataFrame(data)
    
    # Calculate toll rates and print the updated DataFrame
    toll_df = calculate_toll_rate(df)
    print(toll_df)
