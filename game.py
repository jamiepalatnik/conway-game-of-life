from tabulate import tabulate

def main():

    grid = create_grid()
    # main loop
    #while True:
    # Check 
    check_grid(grid)
    # Update

    # Print: Use tabulate to pretty print the grid
    print(tabulate(grid, tablefmt="heavy_grid"))

def create_grid():
    # Define alive and dead cells: alive is 1, dead is 0

    # Define list of lists for the table
    seed_grid = [[0, 0, 0, 0, 0], 
                [0, 0, 1, 0, 0], 
                [0, 1, 1, 0, 0],
                [0, 0, 1, 1, 0], 
                [0, 0, 0, 0, 0]]

    grid = seed_grid
    return grid

# Count live neighbors for each cell (position x, y) in grid
def count_neighbors(x, y, grid):
    live_count = 0
    neighbor_points = [(x-1,y-1), (x-1,y),(x-1,y+1), (x,y-1), (x,y+1), (x+1,y-1), (x+1,y), (x+1,y+1)]
    for pt in neighbor_points:
        try:
            live_count += grid[pt[0]][pt[1]]
        except:
            pass
    return live_count

def check_grid(grid):
    new_grid = []
    for x in range(4):
        for y in range(4):
            n = count_neighbors(x, y, grid)
            print(f"({x}, {y}) - live neighbors found:{n}")
    return new_grid

def apply_rules(n):
    # Define rules of underpopulation, overpopulation, loneliness
    """1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    2. Any live cell with two or three live neighbours lives on to the next generation.
    3. Any live cell with more than three live neighbours dies, as if by overpopulation.
    4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.""" 

    # apply rules
    if cell == 1:
        if n < 2 or n > 3:
            cell = 0

    if cell == 0:
        if n == 3:
            cell = 1

    # TODO: Apply rules to each position in grid

if __name__ == "__main__":
    main()
