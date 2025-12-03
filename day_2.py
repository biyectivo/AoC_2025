import re

result_part1 = 0
result_part2 = 0

#with open(r"C:\Users\biyec\OneDrive\Documentos\Programación\Advent of Code\2025\day_2_sample.txt") as file:
with open(r"C:\Users\biyec\OneDrive\Documentos\Programación\Advent of Code\2025\day_2.txt") as file:
    for line in file:
        ranges = line.strip().split(",")
        for r in ranges:
            if r != "":
                for id in range(int(r.split("-")[0]), int(r.split("-")[1]) + 1):
                    if re.match(r"^(\d+)\1$", str(id)):
                        #print(f"id Match")
                        result_part1 += id

                    if re.match(r"^(\d+)\1+$", str(id)):
                        #print(f"id Match")
                        result_part2 += id

print(result_part1)
print(result_part2)
