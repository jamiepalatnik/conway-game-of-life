from tabulate import tabulate

# Define alive and dead, alive is 1, dead is 0
alive = 1
dead = 0 

# Define array of arrays for the table

seed_grid = [[0, 0, 0, 0, 0], 
             [0, 0, 1, 0, 0], 
             [0, 1, 1, 0, 0],
             [0, 0, 1, 1, 0], 
             [0, 0, 0, 0, 0]]

# Define rules of underpopulation, overpopulation, loneliness
def count_neighbors(x, y):
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
            n = count_neighbors(x,y)
            print(f"({x}, {y}) - live neighbors found:{n}")
            # apply rules

# main loop
grid = seed_grid
#while True:
# Check 
check_grid(grid)
# Update

# Print: Use tabulate to pretty print the grid
print(tabulate(seed_grid, tablefmt="heavy_grid"))
