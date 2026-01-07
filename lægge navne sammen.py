listeofnames = ["tom", "louise", "anna", "mikkel", "ronnie", "simon"] # List of names


def additionOfNames(listeofnames): # Define a function to concatenate names
    collectiveofnames = "" # Initialize an empty string to hold the combined names
    for names in listeofnames: # Loop through each name in the list
        collectiveofnames=  collectiveofnames + names # Concatenate each name with a space
    return collectiveofnames # Return the combined names

additionOfNames(listeofnames) # Call the function with the list of names
print("The sum is:", additionOfNames(listeofnames)) # Print the result of the function call