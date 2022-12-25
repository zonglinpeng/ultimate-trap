import math
import pandas as pd
from pprint import pprint
from collections import Counter
from tabulate import tabulate
from functools import lru_cache

class UTrap:
    def __init__(self) -> None:
        self.data_path = "./asset/data.xlsx"

    def load(self):
        return pd.read_excel(self.data_path).to_numpy()

    def beautify(self):
        grid = self.load()
        data = []
        print_data = []
        row_counter = 0
        print_data.append(["*"] + [str(i) for i in range(len(grid[0]))])
        for y in grid:
            data.append([x for x in y])
            print_data.append([row_counter] + [x for x in y])
            row_counter += 1
        print(tabulate(print_data))
        return data

    def solve(self):
        grid = self.beautify()

        Y = len(grid)
        X = len(grid[0])

        directions = {
            "E":(1,0),
            "W":(-1,0),
            "S":(0,1),
            "N":(0,-1),
            "SE":(1,1),
            "NW":(-1,-1),
            "SW":(-1,1),
            "NE":(1,-1),
        }
        visited = set()
        trace = []

        def is_in_bound(x, y):
            return x < X and y < Y and x >= 0 and y >= 0

        def is_exit(x, y):
            if is_in_bound(x, y) and math.isfinite(grid[y][x]):
                return False
            for x_d, y_d in directions.values():
                x_n = x + x_d
                y_n = y + y_d
                if is_in_bound(x_n, y_n) and not math.isnan(grid[y_n][x_n]):
                    return True
            return False

        def exit_border():
            for y, l in enumerate(grid):
                rst = [(x, y) for x, _ in enumerate(l) if is_exit(x, y)]
                print(rst)

        @lru_cache(maxsize=None)
        def dfs(x, y, direction_name="START"):
            if math.isnan(grid[y][x]):
                return
            cur_val = int(grid[y][x])
            visited.add((x, y))
            trace.append((str(cur_val), x, y, direction_name))
            for direction, (x_delta, y_delta) in directions.items():
                x_new = x_delta * cur_val + x
                y_new = y_delta * cur_val + y
                x_temp, y_temp = x, y
                continue_flag = False

                # check tracing
                while abs(x_new - x_temp) > 0 or abs(y_new - y_temp) > 0:
                    if not is_in_bound(x_temp, y_temp) or math.isnan(grid[y_temp][x_temp]):
                        continue_flag = True
                    x_temp += x_delta
                    y_temp += y_delta
                if continue_flag:
                    continue
                if is_exit(x_new, y_new):
                    print(len(trace))
                    if len([x for x, y in Counter(trace).items() if y > 1]) == 0:
                        pprint(trace)
                        print(("EXIT", x_new, y_new))
                    print(f"----------------\n")

                elif is_in_bound(x_new, y_new) and (x_new, y_new) not in visited:
                    dfs(x_new, y_new, direction)

            visited.remove((x, y))
            trace.pop()

        # print(exit_border())
        dfs(X//2, Y//2)


if __name__ == "__main__":
    UTrap().solve()

