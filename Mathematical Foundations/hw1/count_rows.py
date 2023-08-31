"""
to count how many rows of data in the given dataset

This is for hw1_15/16/17, where I input all the data in the terminal instead of reading the file into the program.
Enter "hi" to specify the end of your data.
"""
co=0
while True:
    tmp=input()
    if tmp == "hi":
        break
    co += 1
print(co)
