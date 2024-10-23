#Question 3: Flatten a Nested Dictionary
def flatten_dictionary(nested_dict, parent_key='', sep='.'):
    items = []  # This will hold the flattened items
    
    # Iterate over each key, value pair in the nested dictionary
    for key, value in nested_dict.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key  # Build the new key
        
        if isinstance(value, dict):  # If the value is a dictionary, recurse into it
            items.extend(flatten_dictionary(value, new_key, sep=sep).items())
        elif isinstance(value, list):  # If the value is a list, iterate over its elements
            for i, item in enumerate(value):
                if isinstance(item, dict):  # If the item is a dictionary, recurse into it
                    items.extend(flatten_dictionary(item, f"{new_key}[{i}]", sep=sep).items())
                else:  # If it's not a dictionary, just add it
                    items.append((f"{new_key}[{i}]", item))
        else:  # If it's a base case (not a dict or list), just add it
            items.append((new_key, value))
    
    return dict(items)  # Convert the list of items back into a dictionary

# Example usage
if __name__ == "__main__":
    # Input nested dictionary
    input_dict = {
        "road": {
            "name": "Highway 1",
            "length": 350,
            "sections": [
                {
                    "id": 1,
                    "condition": {
                        "pavement": "good",
                        "traffic": "moderate"
                    }
                }
            ]
        }
    }
    
    # Flatten the nested dictionary
    flattened_dict = flatten_dictionary(input_dict)
    
    # Print the flattened dictionary
    print(flattened_dict)
    # Expected Output:
    # {
    #     "road.name": "Highway 1",
    #     "road.length": 350,
    #     "road.sections[0].id": 1,
    #     "road.sections[0].condition.pavement": "good",
    #     "road.sections[0].condition.traffic": "moderate"
    # }
