#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
           new_matrix[i][j] = j * j
    return new_matrix
