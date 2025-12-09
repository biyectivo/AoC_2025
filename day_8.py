import re
import math
import numpy as np

result_part1 = 0
result_part2 = 0

boxes = []

limit = 10

with open(r"C:\Users\biyec\OneDrive\Documentos\Programación\Advent of Code\2025\day_8_sample.txt") as file:
#with open(r"C:\Users\biyec\OneDrive\Documentos\Programación\Advent of Code\2025\day_8.txt") as file:
    for line in file:
        boxes.append(tuple(int(x) for x in re.match(r"(\d+),(\d+),(\d+)", line.strip()).groups()))

#print(boxes)

def dist(b1, b2):
    return math.sqrt( (b1[0]-b2[0])**2 + (b1[1]-b2[1])**2 + (b1[2]-b2[2])**2 )

distances = {}
for i in range(len(boxes)):
    for j in range(i+1, len(boxes)):
        d = dist(boxes[i], boxes[j])
        distances[(i,j)] = d

sorted_distances =  sorted(distances.items(), key=lambda x: x[1])
#print(sorted_distances[0:10])


circuits = []

#part 1
for i in range(limit):
    boxes_data = sorted_distances[i][0]
    print(i, "Considering distance ", sorted_distances[i][1], " between boxes ", boxes_data, boxes[boxes_data[0]], boxes[boxes_data[1]] )
    not_present = True
    for j in range(len(circuits)):  
        c = circuits[j]
        not_present = boxes_data[0] not in c and boxes_data[1] not in c
        if not not_present:
            break
    
    if not_present: # no circuit
        circuit = set()
        circuit.add(boxes_data[0])
        circuit.add(boxes_data[1])
        circuits.append(circuit)
    else:
        circuits[j].add(boxes_data[0])
        circuits[j].add(boxes_data[1])

#sorted_circuits = sorted(circuits, key=lambda x: len(x), reverse=True)

# combine any circuits which have at least one member that intersects with any other circuit
check_list = circuits.copy()
i = 0
while i < len(check_list):
    c1 = check_list[i]
    j = i + 1

    merged = False
    while j < len(check_list):
        c2 = check_list[j]
        if len(c1.intersection(c2)) > 0:
            # merge circuits
            c = c1.union(c2)
            check_list.remove(c1)
            check_list.remove(c2)
            check_list.insert(i, c)
            i = 0
            merged = True
            break
        else:
            j += 1
    
    if not merged:
        i += 1

check_list = sorted(check_list, key=lambda x: len(x), reverse=True)

result_part1 = 1
for c in check_list[0:3]:
    result_part1 *= len(c)


print("Final circuits: ", check_list)
print("-------------------------------")
print(result_part1)

