# program that opens a file called “Lab2.txt” for append
with open("Lab2.txt", "a") as file:
    # loop that iterates 5 times
    for index in range(5):
        # asks the user for a person’s name
        name = input("Enter a person's name: ")
        # append the entered name to the output file
        file.write(name + "\n")


