#Question 2: Lists & Dictionaries
def group_strings_by_length(strings):
    length_dict = {}
    
    # Iterate over each string in the input list
    for string in strings:
        length = len(string)  # Get the length of the string
        
        # Add the string to the corresponding length key in the dictionary
        if length not in length_dict:
            length_dict[length] = []  # Initialize the list if the key doesn't exist
        length_dict[length].append(string)  # Append the string to the list
    
    # Sort the dictionary by keys (lengths) and return as a new dictionary
    sorted_length_dict = dict(sorted(length_dict.items()))
    
    return sorted_length_dict

# Example inputs and expected outputs
if __name__ == "__main__":
    # Test cases
    print(group_strings_by_length(["apple", "bat", "car", "elephant", "dog", "bear"]))
    # Expected Output: {3: ['bat', 'car', 'dog'], 4: ['bear'], 5: ['apple'], 8: ['elephant']}
    
    print(group_strings_by_length(["one", "two", "three", "four"]))
    # Expected Output: {3: ['one', 'two'], 4: ['four'], 5: ['three']}
