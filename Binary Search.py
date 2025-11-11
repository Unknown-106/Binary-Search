# Binary Search
# Azhi Amin
# 05/11/2025
# OCR AS Computer Science

#For a binary search, list must be SORTED!
wlist = [i for i in range(1,101)]
print(wlist)

found = False
searchTerm = 42

#first and last pointers
first = 0
last = len(wlist) - 1

#
while found == False and last >= first:
    midpoint = (first + last) // 2
    if searchTerm == wlist[midpoint]:
        found = True
        break
    else:
        if searchTerm > wlist[midpoint]:
            first = midpoint + 1
        elif searchTerm < wlist[midpoint]:
            last = midpoint - 1

#
if found == True:
    print(f"Data item '{searchTerm}' found at position {midpoint}.")
else:
    print(f"Data element '{searchTerm}' not found")

