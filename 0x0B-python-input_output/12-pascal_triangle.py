#!/usr/bin/python3
""" computes apascal triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers in Pascal’s triangle of rows n"""
    if n <= 0:
        return []

    result = [[1]]

    for index in range(n - 1):
        """ add a zero to the  start & end of each row"""
        temp = [0] + result[-1] + [0]
        row = []
        for j in range(len(result[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        result.append(row)
    return result
