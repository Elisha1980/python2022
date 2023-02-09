with open("lab2.txt", "r") as file:
    # split
    allNames = file.read().split("\n")
print(allNames)
# asks the user for a person’s name
name = input("Please enter name: ")
if allNames.__contains__(name):
    print("Name found")
else:
    print("Name not found")

