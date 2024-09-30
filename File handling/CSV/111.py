file = open("Books.csv","w")
newRecord="Book, Author, Year Released\n"
file.write(newRecord)
newRecord="To Kill A Mockingbird, Harper Lee, 1960\n"
file.write(newRecord)
newRecord="A Brief History of Time, Stephen Hawking, 1988\n"
file.write(newRecord)
newRecord="The Great Gatsby, F.Scott Fitzgerald, 1922\n"
file.write(newRecord)
newRecord="The Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985\n"
file.write(newRecord)
newRecord="Pride and Prejudice, Jane Austen, 1813\n"
file.write(newRecord)
file.close()