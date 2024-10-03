
file = open("example.txt", "r")
file2 = open("Book1.csv", "r")

file_content = file.readlines()
file2_content = file2.read()
print(file2_content)
for line in file_content:
    print(line)
    file.close