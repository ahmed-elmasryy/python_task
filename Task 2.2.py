def rotate_matrix_90(matrix):
    n = len(matrix)
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()

def rotate_matrix(matrix, degrees):
    n = len(matrix)
    if degrees == 90:
        rotate_matrix_90(matrix)
    elif degrees == 180:
        rotate_matrix_90(matrix)
        rotate_matrix_90(matrix)
    elif degrees == 270:
        rotate_matrix_90(matrix)
        rotate_matrix_90(matrix)
        rotate_matrix_90(matrix)
    else:
        raise ValueError("Unsupported rotation angle. Use 90, 180, or 270 degrees.")

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_matrix(matrix, 90)
print(matrix)
rotate_matrix(matrix, 180)
print(matrix)
rotate_matrix(matrix, 270)
print(matrix)