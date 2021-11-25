#specify the file you want to check how much character there are in
file = open("Novels.txt","r")

data = file.read()

N = len(data)

print("number of character in this file is:",N)