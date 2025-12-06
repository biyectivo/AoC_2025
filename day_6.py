import re
import numpy as np
from itertools import combinations

result_part1 = 0
result_part2 = 0
matrix = []
matrix_part2 = []
operators = []
#with open(r"C:\Users\biyec\OneDrive\Documentos\Programación\Advent of Code\2025\day_6_sample.txt") as file:
with open(r"C:\Users\biyec\OneDrive\Documentos\Programación\Advent of Code\2025\day_6.txt") as file:
    for line in file:
        if re.match(r"^[0-9 ]+$", line):
            matrix.append( [int(x) for x in re.sub(" {2,}", " ", line.strip()).split(" ") ] )
            matrix_part2.append( [x for x in line.replace("\n","") ] )
        else:
            operators.extend(re.sub(" {2,}", " ", line.strip()).split(" "))

for col in range(len(matrix[0])):
    result = 0 if operators[col] == "+" else 1
    for row in range(len(matrix)):
        if operators[col] == "+":
            result += matrix[row][col]
        elif operators[col] == "*":
            result *= matrix[row][col]
    result_part1 += result


# part 2
matrix_part2 = np.array(matrix_part2)
print(matrix_part2)

cutoffs = []
for i in range(matrix_part2.shape[1]):
    if (matrix_part2[:,i] == " ").all():
        cutoffs.append(i)

print(cutoffs)

start = 0
for i in range(len(cutoffs)+1):
    result = 0 if operators[i] == "+" else 1
    end = matrix_part2.shape[1] if i == len(cutoffs) else cutoffs[i]
    for j in range(start, end):
        num_string = ""
        for row in range(matrix_part2.shape[0]):
            num_string += matrix_part2[row][j]
        int_num = int(num_string)
        #print(int_num)
        if operators[i] == "+":
            result += int_num
        elif operators[i] == "*":
            result *= int_num
    #print(operators[i])
    #print(" Result: " + str(result))
    result_part2 += result
    if i < len(cutoffs):    
        start = cutoffs[i]+1        

print(result_part1)
print(result_part2)
