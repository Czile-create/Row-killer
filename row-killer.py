from fractions import Fraction
import numpy as np
from tabulate import tabulate
import copy
def fraction_printer(a: Fraction): return f'{a.numerator}/{a.denominator}' if a.denominator != 1 else str(a.numerator)

def matrix_printer(matrix):
    a = [map(fraction_printer, i) for i in matrix]
    print(tabulate(a, headers = range(matrix.shape[1]), showindex = "always"))


if __name__ == '__main__':
    n = int(input('Input the number of rows: '))
    m = int(input('Input the number of columns: '))
    print('Input the number of the matrix. \nNote that you should seperate the number of the matrix in the same row with space " ", \nand seperate different rows in enter (i.e. "\\n")')
    matrix = []
    for i in range(n):
        matrix.append([Fraction(i) for i in input().strip().split(' ')])
    matrix = np.array(matrix)
    recorder = []
    while True:
        recorder.append(copy.deepcopy(matrix))
        print('\n')
        print(f'Step {len(recorder)}: ')
        print('=' * 30)
        print()
        matrix_printer(matrix)
        pivot = input('Input the coordinates of the pivot entry\nin the format "row_index, column_index".\nTo quit the program, input "q"; \nTo undo, input "undo"\n> ')
        if pivot == 'q': break
        if pivot == 'undo': 
            try:
                recorder.pop()
                matrix = copy.deepcopy(recorder[-1])
                continue
            except:
                print('Cannot undo in this time!')
                continue
        try:
            i, j = map(int, pivot.split(','))
            matrix[i] *= Fraction(1/matrix[i, j])
            for k in range(matrix.shape[0]):
                if k != i:
                    matrix[k] += matrix[i] * (matrix[k, j] * -1)
        except Exception as e:
            print('An error occurs when processing the row operations.')
            print(e)
            print('We have undoed the changes, try again.')
            matrix = copy.deepcopy(recorder[-1])