# CASE STUDY 1 - Calcualating indexes of submatrixes according to the given data points under some resctrictions
# Time complexity is O(NxM) and space requirement is related to the matrix size

def preprocess(matrix):
    # NxM matrix
    (N, M) = (len(matrix), len(matrix[0]))
    # preprocess the matrix `mat` such that `s[i][j]` stores
    # sum of elements in the matrix from (0, 0) to (i, j)
    s = [[0 for x in range(len(matrix[0]))] for y in range(len(matrix))]
    s[0][0] = matrix[0][0]
    # preprocess the first row
    for j in range(1, len(matrix[0])):
        s[0][j] = matrix[0][j] + s[0][j - 1]
    # preprocess the first column
    for i in range(1, len(matrix)):
        s[i][0] = matrix[i][0] + s[i - 1][0]
    # preprocess the rest of the matrix
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            s[i][j] = matrix[i][j] + s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1]
    return s


def SubmatrixSum(matrix, p, q, r, s):
    matrix = preprocess(matrix)
    # `total` is `mat[r][s] - mat[r][q-1] - mat[p-1][s] + mat[p-1][q-1]`
    total = matrix[r][s]
    if q - 1 >= 0:
        total -= matrix[r][q - 1]
    if p - 1 >= 0:
        total -= matrix[p - 1][s]
    if p - 1 >= 0 and q - 1 >= 0:
        total += matrix[p - 1][q - 1]
    return total


if __name__ == '__main__':
    import numpy as np
    from ast import literal_eval

    R = int(input("number of rows R:"))
    C = int(input("number of columns C:"))
    if 1 > R & C > 500:
        print("# of rows must grater than or equal 1 and # of colums must smaller than or equal 500")
    else:
        while True:
            print("Enter the entries in a single line (separated by space): ")
            entries = list(map(int, input().split()))
            matrix = np.array(entries).reshape(R, C)
            for q in range(1, 100001):
                print("Enter data points point 1 and point2")
                points = input("coordinates as format (p,q) (r,s): ").split()
                coords = [literal_eval(coord) for coord in points]
                if (1 <= (coords[0][0] + 1)) & (coords[1][0] <= (R - 1)) & (1 <= (coords[0][1] + 1)) & (
                        coords[1][1] <= (C - 1)):
                    sum_submtrx = SubmatrixSum(matrix, coords[0][0], coords[0][1], coords[1][0], coords[1][1])
                    print("Offer{}:{}".format(q, sum_submtrx))
                else:
                    print(
                        "p and q must greater than 1 , r must smaller than R and s must smaller than C. Try again")
