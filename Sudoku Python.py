
def is_valid_move(grid, dimension, row, col, num):
    # Calculate subgrid dimensions based on the dimension
    subgrid_rows = dimension // 3 if dimension == 9 else dimension // 4
    subgrid_cols = 3 if dimension == 9 else 4

    for i in range(dimension):
        # Check to see if the number is contained in the same row or column.
        if grid[row][i] == num or grid[i][col] == num:
            return False

    # Calculate the starting row and column of the subgrid
    start_row, start_col = subgrid_rows * \
        (row // subgrid_rows), subgrid_cols * (col // subgrid_cols)

    for i in range(start_row, start_row + subgrid_rows):
        for j in range(start_col, start_col + subgrid_cols):
            if grid[i][j] == num:
                return False

    return True


def solve_sudoku(grid, dimension):
    for i in range(dimension):
        for j in range(dimension):
            if grid[i][j] == 0:
                for num in range(1, dimension + 1):
                    if is_valid_move(grid, dimension, row=i, col=j, num=num):
                        grid[i][j] = num
                        if solve_sudoku(grid, dimension):
                            return True
                        grid[i][j] = 0  # Backtrack here (reset the cell)

                return False  # This line should be at the same level of indentation as the outer for loop

    return True


def print_sudoku(grid):
    for row in grid:
        print(" ".join(map(str, row)))


def sudokuBorders(grid, dimension):
    if dimension == 9:
        for i in range(dimension):
            if i % 3 == 0 and i != 0:
                print("-" * 21)  # Print a horizontal line every 3 rows
            for j in range(dimension):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                print(grid[i][j], end=" ")
            print()

    elif dimension == 12:
        for i in range(dimension):
            if i % 3 == 0 and i != 0:
                print("-" * 32)  # Print a horizontal line every 3 rows
            for j in range(dimension):
                if j % 4 == 0 and j != 0:
                    print("|", end=" ")
                print(grid[i][j], end=" ")
            print()


grid_size_choice = int(input("Grid Dimensions (9 or 12): "))

if ((grid_size_choice != 9) & (grid_size_choice != 12)):
    print("9x9 or 12x12 grids only")
else:
    print("\nPlease input 0 where the Sudoku grid has no values \n")
    rows = grid_size_choice
    cols = grid_size_choice
    # Create an empty matrix, _ acts as a placeholder
    matrix = [[' ' for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):  # Allow the user to fill in the matrix

        print(f"ROW {i+1}: ")

        for j in range(cols):
            value = int(input(f"Enter a value for column {j+1}: "))
        # f before string indicates a formatted string,expressions in curly braces {} are replaced with their actual values at runtime
            matrix[i][j] = value

# Display the filled matrix
    print("Your Sudoku grid: ")
    for row in matrix:
        print(row)

# change arguement (sudoku_grid) based on which grid you want to solve or give your own example
    if solve_sudoku(grid=matrix, dimension=grid_size_choice):
        print("Solved Sudoku:")
        sudokuBorders(grid=matrix, dimension=grid_size_choice)

    else:
        print("No solution exists.")
