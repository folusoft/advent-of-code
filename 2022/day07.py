##try enumerate next time instead of for loop
import pandas as pd
lines = open('day7.txt', 'r').readlines()

def create_fqdn(start, curr_dirs):
    #go from top of the curr_dir to the index and build the path
    path = []
    for index, item in enumerate(curr_dirs):
        if index >= start and index < len(curr_dirs)-1:
            path.insert(0, "/" + item)
    return "".join(x for x in path)

curr_dirs = [] #acts as queue for the directories as we move in and out
dir_content = {}

#change to data gathering between cd and cd .. and then go through and sum up each one
for line in lines:
    line = line.strip()
    is_command = '$' in line
    if is_command:
        command = line.split(' ')[1]
        if command == 'cd':
            dir = dir = line.split(' ')[2]
            if dir == '..': #we've wrapped up in here and now we close out the command
                curr_dirs.pop(0)
            else:
                curr_dirs.insert(0, dir)
                if dir not in dir_content.keys():
                    fqdn = create_fqdn(0, curr_dirs)
                    dir_content[fqdn] = 0
    else:
        #we are listing out what we found in each dir
        #everthing you find in the dir belongs in all the parents in the queue
        size = line.split(' ')[0]
        if size.isdigit():
            for index, dir in enumerate(curr_dirs): 
                fqdn = create_fqdn(index, curr_dirs)
                dir_content[fqdn] += int(size)
       
print(sum([dir_content[x] for x in dir_content if dir_content[x] < 100000]))
print(dir_content[''])

#part b
total_space_available = 70000000
total_space_needed =  30000000
total_space_used = dir_content['']
total_space_unused = total_space_available - total_space_used
total_to_find = total_space_needed - total_space_unused
print(total_to_find)
print(min([dir_content[x] for x in dir_content if dir_content[x] >= total_to_find]))
  
    
            
        