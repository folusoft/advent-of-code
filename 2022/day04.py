
file1 = open('day4.txt', 'r')
lines = file1.readlines()

def contains(l1, l2):
    larger = l1 if len(l1) > len(l2) else l2
    smaller = l2 if len(l1) > len(l2) else l1
    return all(x in larger for x in smaller)

def overlaps(l1, l2):
    larger = l1 if len(l1) > len(l2) else l2
    smaller = l2 if len(l1) > len(l2) else l1
    return any(x in larger for x in smaller)

full_overlaps = 0
partial_overlap = 0
for line in lines:
    p1, p2 = line.strip().split(',')[0], line.strip().split(',')[1]
    range_p1 = [x for x in range(int(p1.split('-')[0]), int(p1.split('-')[1])+1)]
    range_p2 = [x for x in range(int(p2.split('-')[0]), int(p2.split('-')[1])+1)]
    if contains(range_p1, range_p2):
        full_overlaps = full_overlaps + 1
    if overlaps(range_p1, range_p2):
        partial_overlap = partial_overlap + 1

print (full_overlaps)
print (partial_overlap)
