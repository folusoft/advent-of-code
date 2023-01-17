import string
l_alphabet = list(string.ascii_lowercase)
u_alphabet = list(string.ascii_uppercase)

file1 = open('day3.txt', 'r')
lines = file1.readlines()
issues = []
for line in lines:
    line = line.strip()
    half = int(len(line)/2)
    part_a = set(line[0:half])
    part_b = set(line[half:])
    common = list((part_a & part_b))[0]
    if common.islower():
        issues.append(l_alphabet.index(common) + 1)
    else:
         issues.append(u_alphabet.index(common) + 27)

print(sum(issues))

counter = 0
groups = []
issues = []
#part 2
for line in lines:
    line = line.strip()
    counter = counter + 1
    groups.append(set(line))
    if counter % 3 == 0:
        common = list((groups[0] & groups[1] & groups[2]))[0]
        if common.islower():
            issues.append(l_alphabet.index(common) + 1)
        else:
            issues.append(u_alphabet.index(common) + 27)
        groups = []
print(sum(issues))

    
