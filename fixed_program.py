# FIXED version: find the highest mark and the average
marks = [95, 72, 88, 65, 79]

highest = marks[0]
for mark in marks:                  # Fix 1: check every element
    if mark > highest:
        highest = mark

average = sum(marks) / len(marks)   # Fix 2: no stray "- 1"

print("Highest:", highest)
print("Average:", average)
