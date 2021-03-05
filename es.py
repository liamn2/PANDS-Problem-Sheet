# Program to count the occurences of a particular character in a file.
# charactercount.py
# Author: Liam Nutley

k = 0   
e = "e"
 
with open("moby-dick.txt", 'r') as f: 
    # Use open() funtion to open text in desired format. 
    for line in f:
        # f is our file, line goes through its lines.
        words = line.split()
        # line.split()  will create an array of the words in the text. 
        for i in words:
            for letter in i:
                if(letter==e):
                    # Our desired letter is "e"
                    k=k+1
print("Occurrences of the letter:")
# Print result
print(k)