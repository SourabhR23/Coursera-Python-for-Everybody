"""Finding Numbers in a Haystack

In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the 
file and compute the sum of the numbers.

Data Files
We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is 
the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
Actual data: http://py4e-data.dr-chuck.net/regex_sum_565581.txt (There are 77 values and the sum ends with 498)
These links open in a new window. Make sure to save the file into the same folder as you will be writing your Python 
program. Note: Each student will have a distinct data file for the assignment - so only use your own data file for analysis."""

import re

name = input("Enter File: ")
if len(name) < 1 : name = "regex_sum_565581.txt"
    
file = open(name)
sum = 0
for line in file:
    temp = line.rstrip()
    temp = re.findall('[0-9]+', temp)
    if len(temp) > 0:
        for i in temp:
            sum += int(i)
            
print("The sum of numbers in text file is", sum)

