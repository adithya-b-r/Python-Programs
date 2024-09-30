programmes = ["Pokemon","Beyblade","Ninja Hattori","Shinchan"]

for shows in programmes:
    print(shows)

new_show = (input("Enter another show name : "))
programmes.insert(int(input("Enter position : ")), new_show)

print(programmes)