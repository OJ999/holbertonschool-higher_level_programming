def pascal_triangle(n):
    """
    Returns Pascal's triangle of height n.

    Args:
        n (int): Height of the Pascal's triangle.

    Returns:
        list of lists: Pascal's triangle represented as a list of lists of integers.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize with the first row

    for i in range(1, n):
        row = [1]  # Start each row with 1
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])  # Calculate the value based on previous row
        row.append(1)  # End each row with 1
        triangle.append(row)

    return triangle

# Test the function
if __name__ == "__main__":
    n = 5
    triangle = pascal_triangle(n)
    for row in triangle:
        print(row)
