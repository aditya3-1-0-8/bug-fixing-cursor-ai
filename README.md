# Bug Fixing Using Cursor AI

A buggy Python program that was found and corrected using Cursor AI.

## The program
It finds the highest mark and the average of a list of marks.

## Bugs found and fixed
1. **Skipped the first element.** The loop used `range(1, len(marks))`, so `marks[0]` was never checked. If the highest mark was first, the answer was wrong. Fix: loop over every mark and start `highest` from `marks[0]`.
2. **Wrong average.** The code had `total / len(marks) - 1`, which subtracts 1 from the correct average. Fix: remove the `- 1`.

## Output
| | Buggy | Fixed |
|---|---|---|
| Highest | 88 (wrong) | 95 |
| Average | 78.8 (wrong) | 79.8 |

Test data: `[95, 72, 88, 65, 79]`.

## How to run
`python fixed_program.py`

## Technologies
Python 3, Cursor AI

## Author
Aditya Bansal - [GitHub](https://github.com/aditya3-1-0-8)
