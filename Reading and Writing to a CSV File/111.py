import csv

file = open("Books.csv","w")

file.write("To Kill A Mockingbird, Harper Lee, 1960 \n")
file.write("A Brief History of Time, Stephen Hawking, 1988 \n")
file.write("The Great Gatsby, F. Scott Fitzgerald, 1922 \n")
file.write("The Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985 \n")
file.write("Pride and Prejudice, Jane Austen, 1813 \n")

file.close()