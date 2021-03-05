# Program to count the occurences of a particular character in a file.
# charactercount.py
# Author: Liam Nutley

k = 0
e = "e"
 
with open("moby-dick.txt", 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            for letter in i:
                if(letter==e):
                    k=k+1
print("Occurrences of the letter:")
print(k)