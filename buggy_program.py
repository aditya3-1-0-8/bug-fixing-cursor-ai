# BUGGY version: find the highest mark and the average
marks = [95, 72, 88, 65, 79]

highest = 0
for i in range(1, len(marks)):      # Bug 1: skips the first element
    if marks[i] > highest:
        highest = marks[i]

total = 0
for m in marks:
    total += m
average = total / len(marks) - 1    # Bug 2: subtracts 1 by mistake

print("Highest:", highest)
print("Average:", average)
