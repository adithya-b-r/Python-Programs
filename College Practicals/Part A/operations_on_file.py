filename = "sample.txt"

with open(filename, "w") as f:
    f.write("This is the first line of the text.\n"
            "This is the second line of the text.\n"
            "This is the third line of the text.\n")

with open(filename, "r") as f:
    contents = f.read()
    num_chars = len(contents)
    num_words = len(contents.split())
    num_lines = len(contents.splitlines())

print("Number of characters : ", num_chars)
print("Number of words : ", num_words)
print("Number of lines : ", num_lines)
