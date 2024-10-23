#Question 1: Reverse List by N Elements

def reverse_list_by_n_elements(lst, n):
    result = []
    length = len(lst)
    
    # Iterate through the list in steps of n
    for i in range(0, length, n):
        # Get the current chunk
        chunk = lst[i:i+n]
        
        # If the chunk is smaller than n, we just reverse whatever is left
        if len(chunk) < n:
            # Reverse manually
            for j in range(len(chunk)):
                result.append(chunk[len(chunk) - 1 - j])
        else:
            # Reverse manually
            for j in range(n):
                result.append(chunk[n - 1 - j])
    
    return result

# Example inputs and expected outputs
if __name__ == "__main__":
    # Test cases
    print(reverse_list_by_n_elements([1, 2, 3, 4, 5, 6, 7, 8], 3))  # Expected Output: [3, 2, 1, 6, 5, 4, 8, 7]
    print(reverse_list_by_n_elements([1, 2, 3, 4, 5], 2))            # Expected Output: [2, 1, 4, 3, 5]
    print(reverse_list_by_n_elements([10, 20, 30, 40, 50, 60, 70], 4))  # Expected Output: [40, 30, 20, 10, 70, 60, 50]



