#Question 6: Decode Polyline, Convert to DataFrame with Distances

import polyline
import pandas as pd
import numpy as np

def haversine(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    
    # Radius of Earth in meters (mean radius)
    r = 6371000  
    return c * r

def decode_polyline_and_create_dataframe(polyline_str):
    # Decode the polyline string into a list of (latitude, longitude) coordinates
    decoded_points = polyline.decode(polyline_str)

    # Initialize lists to hold latitudes, longitudes, and distances
    latitudes = []
    longitudes = []
    distances = [0]  # First distance is 0 as there is no previous point

    # Loop through the decoded points to extract latitude and longitude
    for i, (lat, lon) in enumerate(decoded_points):
        latitudes.append(lat)
        longitudes.append(lon)

        if i > 0:  # Calculate distance for points after the first one
            dist = haversine(latitudes[i-1], longitudes[i-1], lat, lon)
            distances.append(dist)

    # Create a DataFrame with the results
    df = pd.DataFrame({
        'latitude': latitudes,
        'longitude': longitudes,
        'distance': distances
    })

    return df

# Example usage
polyline_str = "a~l~Fjk~uOwHJy@d@?n@"
df = decode_polyline_and_create_dataframe(polyline_str)
print(df)
