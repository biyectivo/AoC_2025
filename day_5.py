import re
import numpy as np

result_part1 = 0
result_part2 = 0

ranges = []

def check_in_range(n, r):
    start = int(r.split("-")[0])
    end = int(r.split("-")[1])
    return n >= start and n <= end

def check_in_ranges(n):
    global ranges
    for r in ranges:
        if check_in_range(n, r):
            return True
    return False
        
#with open(r"C:\Users\biyec\OneDrive\Documentos\Programación\Advent of Code\2025\day_5_sample.txt") as file:
#with open(r"C:\Users\biyec\OneDrive\Documentos\Programación\Advent of Code\2025\day_5_sample_2.txt") as file:
with open(r"C:\Users\biyec\OneDrive\Documentos\Programación\Advent of Code\2025\day_5.txt") as file:
    for line in file:
        if line != "\n":
            if line.find("-") != -1:
                ranges.append(line.strip())
            else:
                if check_in_ranges(int(line)):
                    result_part1 += 1


def range_intersect(r1, r2):
    start1 = int(r1.split("-")[0])
    end1 = int(r1.split("-")[1])
    start2 = int(r2.split("-")[0])
    end2 = int(r2.split("-")[1])
    return not (end1 < start2 or end2 < start1)

check_ranges = ranges.copy()
i = 0
while i < len(check_ranges):
    r1 = check_ranges[i]
    j = i + 1
    
    merged = False
    while j < len(check_ranges):
        r2 = check_ranges[j]

        if range_intersect(r1, r2):
            new_start = min(int(r1.split("-")[0]), int(r2.split("-")[0]))
            new_end = max(int(r1.split("-")[1]), int(r2.split("-")[1]))
            new_range = f"{new_start}-{new_end}"
            check_ranges.remove(r1)
            check_ranges.remove(r2)
            check_ranges.insert(i, new_range)
            i = 0
            merged = True
            break
        else:
            j += 1
    
    if not merged:
        i += 1


for r in check_ranges:
    start = int(r.split("-")[0])
    end = int(r.split("-")[1])
    if r != "0-0" and (end - start + 1) > 0:
        result_part2 += (end - start + 1)
        #print("Partial result: ", result_part2)

print(result_part1)
print(result_part2)
