#Question 13: Calculate Time-Based Toll Rates

import pandas as pd
import numpy as np
import datetime

def calculate_time_based_toll_rates(df):
    # Define discount factors based on time intervals
    weekday_discount_factors = {
        (datetime.time(0, 0), datetime.time(10, 0)): 0.8,
        (datetime.time(10, 0), datetime.time(18, 0)): 1.2,
        (datetime.time(18, 0), datetime.time(23, 59, 59)): 0.8,
    }
    weekend_discount_factor = 0.7

    # Initialize new columns
    start_days = []
    start_times = []
    end_days = []
    end_times = []

    # Define the days of the week
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Assume the input DataFrame has columns: id_start, id_end, distance, and vehicle columns
    for index, row in df.iterrows():
        # Example logic to determine the start and end days and times
        # Here we are using dummy values; you should replace these with your logic
        start_day = "Monday"  # Replace with actual logic to determine start day
        start_time = datetime.time(9, 0)  # Example start time: 09:00 AM
        end_day = "Monday"  # Replace with actual logic to determine end day
        end_time = datetime.time(17, 0)  # Example end time: 05:00 PM

        # Update new lists for days and times
        start_days.append(start_day)
        start_times.append(start_time)
        end_days.append(end_day)
        end_times.append(end_time)

        # Apply discount based on the time of day
        # Weekday logic
        if start_day in days_of_week[:5]:  # Monday to Friday
            # Check the applicable discount based on start time
            for time_range, discount in weekday_discount_factors.items():
                if time_range[0] <= start_time < time_range[1]:
                    for vehicle in ['moto', 'car', 'rv', 'bus', 'truck']:
                        # Adjusting the rate based on the discount factor
                        df.at[index, vehicle] *= discount
                    break  # Break after applying the discount
        else:  # Weekend logic (Saturday and Sunday)
            for vehicle in ['moto', 'car', 'rv', 'bus', 'truck']:
                df.at[index, vehicle] *= weekend_discount_factor

    # Add new columns to the DataFrame
    df['start_day'] = start_days
    df['start_time'] = start_times
    df['end_day'] = end_days
    df['end_time'] = end_times

    return df

# Example usage
if __name__ == "__main__":
    # Sample DataFrame based on Question 12
    data = {
        'id_start': ['A', 'A', 'B', 'B', 'C', 'D'],
        'id_end': ['B', 'C', 'A', 'D', 'D', 'A'],
        'distance': [5, 8, 5, 7, 10, 6],
        'moto': [4.0, 6.4, 4.0, 5.6, 8.0, 4.8],
        'car': [6.0, 9.6, 6.0, 8.4, 12.0, 7.2],
        'rv': [7.5, 12.0, 7.5, 10.5, 15.0, 9.0],
        'bus': [11.0, 17.6, 11.0, 15.4, 22.0, 13.2],
        'truck': [18.0, 28.8, 18.0, 25.2, 36.0, 21.6]
    }

    df = pd.DataFrame(data)

    # Calculate time-based toll rates and print the updated DataFrame
    updated_df = calculate_time_based_toll_rates(df)
    print(updated_df)
