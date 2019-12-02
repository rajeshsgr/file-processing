with open("one.txt", "a+") as file :
    file.write("\nFour")
    file.seek(0)
    content=file.read()

print(content)