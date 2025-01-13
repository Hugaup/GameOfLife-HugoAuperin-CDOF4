import os
import time
import random

def create_grid(rows, cols, randomise=False):
    """Create a grid with the specified number of rows and columns."""
    if randomise:
        return [[random.choice([' ', '#']) for _ in range(cols)] for _ in range(rows)]
    else:
        return [[' ' for _ in range(cols)] for _ in range(rows)]

def print_grid(grid):
    """Print the grid to the console."""
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        print(''.join(row))

def count_live_neighbours(grid, x, y):
    """Count the number of live neighbours for a cell at position (x, y)."""
    rows, cols = len(grid), len(grid[0])
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),         (0, 0),
        (1, -1), (1, 0), (1, 1)
    ]
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '#':
            count += 1
    return count

def update_grid(grid):
    """Update the grid based on Conway's Game of Life rules."""
    rows, cols = len(grid), len(grid[0])
    new_grid = create_grid(rows, cols)

    for x in range(rows):
        for y in range(cols):
            live_neighbours = count_live_neighbours(grid, x, y)

            if grid[x][y] == '#':
                # Any live cell with 2 or 3 live neighbours survives.
                if live_neighbours in [2, 3]:
                    new_grid[x][y] = '#'
                else:
                    new_grid[x][y] = ' '
            else:
                # Any dead cell with exactly 3 live neighbours becomes a live cell.
                if live_neighbours == 3:
                    new_grid[x][y] = '#'
                else:
                    new_grid[x][y] = ' '

    return new_grid

def main():
    rows, cols = 20, 40  # Dimensions of the grid
    grid = create_grid(rows, cols, randomise=True) # Create a random grid

    try:
        while True:
            print_grid(grid)
            grid = update_grid(grid)
            time.sleep(0.5)  # Pause for a moment to observe the updates
    except KeyboardInterrupt:
        print("\nGame stopped.")

if __name__ == "__main__":
    main()
