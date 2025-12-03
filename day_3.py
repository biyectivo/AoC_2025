import re

result_part1 = 0
result_part2 = 0

#with open(r"C:\Users\biyec\OneDrive\Documentos\Programación\Advent of Code\2025\day_3_sample.txt") as file:
with open(r"C:\Users\biyec\OneDrive\Documentos\Programación\Advent of Code\2025\day_3.txt") as file:
    for line in file:
        line = line.strip()
        #part 1 - for two digit, find max digit as long as its not in the last position = length-1 = length-(2-1)
        length = len(line)
        tens_digit = 9
        found = False
        while tens_digit > 0 and not found:
            pos = line.find(str(tens_digit))
            if pos != -1 and pos < length-1:
                found = True
            else:
                tens_digit -= 1
        unit_digit = max(d for d in line[pos+1:])
        result_part1 += int(str(tens_digit) + unit_digit)

        #part 2 - do the same 12 times...
        number = ""

        evaluation_string = line
        length = len(evaluation_string)
        for i in range(12):
            tens_digit = 9
            found = False
            while tens_digit > 0 and not found:
                pos = evaluation_string.find(str(tens_digit))
                if pos != -1 and pos < length-(11-i):
                    found = True
                else:
                    tens_digit -= 1
            number += str(tens_digit)
            evaluation_string = evaluation_string[pos+1:]
            length = len(evaluation_string)
        
        result_part2 += int(number)

print(result_part1)
print(result_part2)
