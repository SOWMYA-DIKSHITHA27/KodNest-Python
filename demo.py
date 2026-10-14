#reading the complete file using read
# file = open("demo.txt", "r")
# data = file.read()
# print(data)
# file.close()

#reading the file using readline
# file = open("demo.txt", "r")
# data = file.readline()
# print(data)
# file.close()
#reading the files all lines using loop
file = open("demo.txt", "r")
for line in file:
    print(line.strip())
file.close()