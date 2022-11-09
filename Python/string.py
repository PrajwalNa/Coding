"""
Dev: Prajwal Nautiyal
Last Update: 8 November 2022
"""

name = input("Enter your string: ")
l = len(name)                                               # Length of the string
newN = name.upper()                                         # Changed the case so it doesn't cause issues with equivalency
arr = []                                                    # list to store the repeated letters
arrN = []                                                   # list to store number of repetitions
for c in newN:
    i = 0                                                   # counter variable
    j = 0                                                   # loop variable
    if c != " ":                                            # Conditional check for spaces in between words
        for j in range(l):                                  # Loop to check the number of repetitions
            if c == newN[j]:                                # Conditional check for equivalency
                i += 1                                      # Incrementing the counter variable
    if i > 1 and c not in arr:                              # Check for increased counter and to avoid printing two of the same letter
        arr.append(c)                                       # Appending the letter to the list
        arrN.append(i-1)                                    # i-1 since we only need the number of repetitions excluding the first appearance

print("\n")                                                 # String for seperation
for c in range(len(arr)):
    print(f"{arr[c]} is repeated {arrN[c]} time(s)")        # Using indexing to print the relevant values