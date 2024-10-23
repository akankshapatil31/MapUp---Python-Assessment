#Question 4: Generate Unique Permutations

def permute_unique(nums):
    def backtrack(path, used):
        if len(path) == len(nums):
            result.append(path[:])  # Append a copy of the current permutation to the result
            return
        
        for i in range(len(nums)):
            # Skip used elements
            if used[i]:
                continue
            
            # Skip duplicates: if the current element is the same as the previous element
            # and the previous element was not used, skip this element to avoid duplicates
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue
            
            used[i] = True  # Mark the element as used
            path.append(nums[i])  # Add the current number to the path
            
            backtrack(path, used)  # Recur
            path.pop()  # Backtrack: remove the last element
            used[i] = False  # Mark the element as unused for the next iterations
    
    result = []
    nums.sort()  # Sort the numbers to handle duplicates easily
    used = [False] * len(nums)  # Track used elements
    backtrack([], used)  # Start backtracking with an empty path
    return result

# Example usage
if __name__ == "__main__":
    # Input list of integers
    input_list = [1, 1, 2]
    
    # Generate unique permutations
    unique_permutations = permute_unique(input_list)
    
    # Print the result
    for permutation in unique_permutations:
        print(permutation)

    # Expected Output:
    # [1, 1, 2]
    # [1, 2, 1]
    # [2, 1, 1]
