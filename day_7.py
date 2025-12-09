import re
import numpy as np
import functools

result_part1 = 0
result_part2 = 0

def valid(row, col):
    global map_data
    return 0 <= row < map_data.shape[0] and 0 <= col < map_data.shape[1]


def beam_starting_from(row, col):
    global map_data, result_part1, result_part2
    
    if not valid(row, col):
        return False
    
    dx = 0
    dy = 1
    new_row = row + dy
    new_col = col + dx

    while valid(new_row, new_col) and map_data[new_row, new_col] == ".":
        map_data[new_row, new_col] = "|"
        new_row += dy
        new_col += dx

    
    if valid(new_row, new_col) and map_data[new_row, new_col] == "^":
        result_part1 += 1
        if valid(new_row, new_col-1):
            map_data[new_row, new_col-1] = "|"
            beam_starting_from(new_row, new_col-1)
            
        if valid(new_row, new_col+1):
            map_data[new_row, new_col+1] = "|"
            beam_starting_from(new_row, new_col+1)

timelines = set()

memoization = {}

def count_paths(row, col, timeline=()):
    global map_data, timelines
    
    timeline += (int(row), int(col))
    if not valid(row, col):
        #print(timeline)
        timelines.add(tuple(timeline))
        return 1
    elif map_data[row, col] == "^":
        return count_paths(row, col + 1, timeline) + count_paths(row, col - 1, timeline)
    else:
        if (row, col) in memoization:
            return memoization[(row, col)]
        else:
            result = count_paths(row + 1, col, timeline)
            memoization[(row, col)] = result
            return result



map_data = []
#with open(r"C:\Users\biyec\OneDrive\Documentos\Programación\Advent of Code\2025\day_7_sample.txt") as file:
#with open(r"C:\Users\biyec\OneDrive\Documentos\Programación\Advent of Code\2025\day_7_sample_2.txt") as file:
with open(r"C:\Users\biyec\OneDrive\Documentos\Programación\Advent of Code\2025\day_7.txt") as file:
    for line in file:
        map_data.append([x for x in line.strip()])
map_data = np.array(map_data)

start_row = (np.where(map_data == "S")[0][0])
start_col = (np.where(map_data == "S")[1][0])
#print(start_row, start_col)
beam_starting_from(start_row, start_col)
result_part2 = count_paths(start_row, start_col)

print(result_part1)
print(result_part2)