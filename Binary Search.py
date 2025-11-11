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

#checks if the midpoint of the current section of the list is the searchTerm, if not checks if the searchTerm is before or after the midpoint and updates the first/last positions accordingly
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

#Once narrowed down, prints the searchTerm and the position it was found at, or 'not found' if searchTerm is not found in the list
if found == True:
    print(f"Data item '{searchTerm}' found at position {midpoint}.")
else:
    print(f"Data element '{searchTerm}' not found")
