"""8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the 
following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person 
who sent the message). Then print out a count at the end.Hint: make sure not to include the lines that start with 'From:'.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt"""

file_input = input("")
file_open = open(file_input)
count = 0
for i in file_open:
    if i.startswith("From "):
        new = i.rstrip().split()
        email = new[1]
        print(email)
        count += 1
    else:
        continue
print("There were", count, "lines in the file with From as the first word")
