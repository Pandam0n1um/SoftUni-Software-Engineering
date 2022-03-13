def get_magic_triangle(n):
    triangle = [[1]]
    for row in range(2, n+1):
        triangle.append([])
        for col in range(row):
            left_neighbor = (sum(triangle[row - 2][col - 1:col]) if triangle[row - 2][col - 1:col] else 0)
            right_neighbor = (sum(triangle[row - 2][col:col + 1]) if triangle[row - 2][col:col + 1] else 0)

            triangle[row-1].append(left_neighbor + right_neighbor)
    return triangle


get_magic_triangle(5)
