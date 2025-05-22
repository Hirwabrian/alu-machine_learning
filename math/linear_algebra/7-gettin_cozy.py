def cat_matrices2D(mat1, mat2, axis=0):
    # Concatenate vertically (add more rows)
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        result = []
        for row in mat1:
            result.append(row[:])
        for row in mat2:
            result.append(row[:])
        return result

    # Concatenate horizontally (add more columns to each row)
    elif axis == 1:
        if len(mat1) != len(mat2):
            return None
        result = []
        for i in range(len(mat1)):
            result.append(mat1[i] + mat2[i])
        return result

    return None
