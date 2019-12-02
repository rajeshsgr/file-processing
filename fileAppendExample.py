import os

if os.path.exists("one.txt") :
    with open("one.txt", "a+") as file :
        file.write("\nFour")
        file.seek(0)
        content=file.read()

    print(content)