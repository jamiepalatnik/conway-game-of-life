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


# Check 

# Update

# Print: Use tabulate to pretty print the grid
print(tabulate(seed_grid, tablefmt="heavy_grid"))