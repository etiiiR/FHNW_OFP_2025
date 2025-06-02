from typing import Callable, Generator, Tuple
from functools import partial
import time
import os

Grid = Tuple[Tuple[bool, ...], ...]
Cell_Check = Callable[[int, int], bool]
Rule = Callable[[Cell_Check, int, int], bool]
Step_Function = Callable[[Grid], Grid]

conway_rule: Rule = lambda cell, x, y: (
    (n := sum(
        cell(x + dx, y + dy)
        for dx in (-1, 0, 1)
        for dy in (-1, 0, 1)
        if (dx, dy) != (0, 0)
    )) == 3 or (cell(x, y) and n == 2)
)

make_cell_checker: Callable[[Grid], Cell_Check] = lambda grid: (
    lambda x, y: 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y]
)

step_func: Callable[[Rule], Step_Function] = lambda rule: (
    lambda grid: _step_recursive(grid, rule, 0)
)

def _step_recursive(grid: Grid, rule: Rule, x: int) -> Grid:
    if x >= len(grid):
        return ()
    check = make_cell_checker(grid)
    row = _row_recursive(grid, rule, check, x, 0)
    return (row,) + _step_recursive(grid, rule, x + 1)

def _row_recursive(grid: Grid, rule: Rule, check: Cell_Check, x: int, y: int) -> Tuple[bool, ...]:
    if y >= len(grid[0]):
        return ()
    return (rule(check, x, y),) + _row_recursive(grid, rule, check, x, y + 1)

def steps(start: Grid, step: Step_Function) -> Generator[Grid, None, None]:
    def loop(current: Grid) -> Generator[Grid, None, None]:
        yield current
        yield from loop(step(current))
    return loop(start)

def display(grid: Grid) -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    top = "┌" + "─" * len(grid[0]) + "┐"
    bottom = "└" + "─" * len(grid[0]) + "┘"
    print(top)
    for row in grid:
        line = "".join(
            "\033[92m█\033[0m" if c else " " for c in row
        )
        print("│" + line + "│")
    print(bottom)

parse_grid: Callable[[Tuple[str, ...]], Grid] = lambda lines: (
    tuple(tuple(c == '#' for c in line.strip()) for line in lines)
)

def main():
    lines = (
        "....................",
        "....###...##........",
        "...#..#..##..#......",
        "...#..#..#...#......",
        "....###...###.......",
        "....................",
        "...###..............",
        "....#...............",
        "...###..............",
        "....................",
    )
    grid = parse_grid(lines)
    step = step_func(conway_rule)
    gen_iter = steps(grid, step)
    last = None
    for _ in range(1000):
        current = next(gen_iter)
        display(current)
        if current == last:
            print("Keine Änderung mehr – Spiel beendet.")
            break
        last = current
        time.sleep(0.1)

if __name__ == "__main__":
    main()