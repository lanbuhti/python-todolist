file = open("essay.txt", "r")
content = file.read()
print(content.title())
print(len(content))
file.close()