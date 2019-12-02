
with open("sample.txt") as fileSample :

    content= fileSample.read()


print("Count of total characters in the file :" ,len(content))

print("Number of occurence of character 'r' :" , content.count("a"))

print("Printing first 100 characters: ")

print(content[:100])