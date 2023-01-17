import pandas as pd

file1 = open('day1.txt', 'r')
lines = file1.readlines()

elves = dict()

elf = {}
counter = 1
for line in lines:
    elf_name = f'elf {counter}'
    if len(line) < 2:
        #we've reached the end of an elf
        counter = counter + 1
        continue
   
    calories = int(line)
    if elf_name in elves.keys():
        elves[elf_name]['calories'] = elves[elf_name].get('calories') + calories
    else:
        elves[elf_name] = {'elf_name' : elf_name, 'calories' : calories}

df = pd.DataFrame(elves.values())
print(df.calories.max())
print("part 2")
top_3 = df.nlargest(3, 'calories')
print(top_3['calories'].sum())
