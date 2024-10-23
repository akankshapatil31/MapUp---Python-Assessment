#Question 7: Matrix Rotation and Transformation

def rotate_matrix(matrix):
    n = len(matrix)
    # Create a new matrix to hold the rotated version
    rotated = [[0] * n for _ in range(n)]

    # Perform the rotation
    for i in range(n):
        for j in range(n):
            rotated[j][n - 1 - i] = matrix[i][j]

    return rotated

def transform_matrix(rotated_matrix):
    n = len(rotated_matrix)
    # Create a new matrix to hold the transformed version
    transformed = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            # Calculate sum of row i and column j, excluding the current element
            row_sum = sum(rotated_matrix[i]) - rotated_matrix[i][j]
            col_sum = sum(rotated_matrix[k][j] for k in range(n)) - rotated_matrix[i][j]
            transformed[i][j] = row_sum + col_sum

    return transformed

def process_matrix(matrix):
    rotated = rotate_matrix(matrix)
    final_matrix = transform_matrix(rotated)
    return final_matrix

# Example usage
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = process_matrix(matrix)
for row in result:
    print(row)
