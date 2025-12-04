import re
import numpy as np

result_part1 = 0
result_part2 = 0

my_map = []

def is_valid(row, col):
    global my_map
    return not(row < 0 or row >= my_map.shape[0] or col < 0 or col >= my_map.shape[1])

def count_adjacent(map, row, col):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]
    count = 0
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if is_valid(r, c) and map[r][c] == '@':
            count += 1
    return count

#with open(r"C:\Users\biyec\OneDrive\Documentos\Programación\Advent of Code\2025\day_4_sample.txt") as file:
with open(r"C:\Users\biyec\OneDrive\Documentos\Programación\Advent of Code\2025\day_4.txt") as file:
    for line in file:
        line = line.strip()
        my_map.append([c for c in line])

my_map = np.array(my_map)

for row in range(my_map.shape[0]):
    for col in range(my_map.shape[1]):
        if my_map[row, col] == "@" and count_adjacent(my_map, row, col) < 4:
            result_part1 += 1

num_removed = 0
iterations = 0
starting_map = my_map.copy()
while iterations == 0 or num_removed > 0:
    #print(iterations, starting_map)
    new_map = starting_map.copy()
    num_removed = 0
    for row in range(my_map.shape[0]):
        for col in range(my_map.shape[1]):
            if starting_map[row, col] == "@" and count_adjacent(starting_map, row, col) < 4:
                new_map[row, col] = "x"
                num_removed += 1
                result_part2 += 1
    #print("Removed this iteration:", num_removed)
    iterations += 1
    starting_map = new_map.copy()

#print(my_map)

print(result_part1)
print(result_part2)
