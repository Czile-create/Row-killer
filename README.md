# Row-killer
Kill another row in the matrix using a specific pivot entry. This is a step in Gaussian elimination.

We select a pivot entry and apply row operations in the matrix such that:

- The pivot entry is transformed to 1, by multiplying the multiplicative inverse $x^{-1}$ to the row that the pivot entry is in.
- The other entry that is in the same column as the pivot entry comes to 0, by adding the multiplicative inverse of these elements times the pivot row to these rows.

## Usage
First, you enter the number of rows and columns of your matrix.

You then choose a pivot element to kill the other row, by entering the index in the format (row, column)

We display the operations in rational numbers precisely.

We can always undo by entering "undo"
