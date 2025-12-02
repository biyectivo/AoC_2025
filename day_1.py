import re

result_part1 = 0

current = 50

result_part2 = 0

with open(r"C:\Users\biyec\OneDrive\Documentos\Programación\Advent of Code\2025\day_1.txt") as file:
#with open(r"C:\Users\biyec\OneDrive\Documentos\Programación\Advent of Code\2025\day_1_sample.txt") as file:
    for line in file:
        line = line.strip()
        match = re.match("([LR])(\d+)", line)
        sign = 1 if match.group(1) == "R" else -1
        num = int(match.group(2))
        
        i=1
        current2 = current
        while i<=num:
            current2 = (100 + current2 + sign*1) % 100
            if current2 == 0:
                result_part2 += 1
            i+=1
        
        current = (100 + current + sign * num) % 100
        if current == 0:
            result_part1 += 1
        
        
print(result_part1)
print(result_part2)
        

