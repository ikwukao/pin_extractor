# Function to extract secret PIN codes from a list of poems
def pin_extractor(poems):
    
    # This list will store the final secret codes
    # generated from each poem
    secret_codes = []    
    
    # Loop through each poem in the poems list
    for poem in poems:
        
        # This will hold the secret code for the current poem
        secret_code = ""
        
        # Split the poem into individual lines
        # '\n' represents a new line character
        lines = poem.split('\n')

        # enumerate() gives both:
        # 1. the line index (0, 1, 2, ...)
        # 2. the actual line content
        for line_index, line in enumerate(lines):
            
            # Split the current line into separate words
            words = line.split()
            
            # Check if the current line contains enough words
            # to access the word at position "line_index"
            #
            # Example:
            # line_index = 2
            # We need at least 3 words in the line
            if len(words) > line_index:
                
                # Get the word at the matching index
                # Then count the number of characters in that word
                #
                # Example:
                # words[2] -> "moon"
                # len("moon") -> 4
                #
                # Convert the number to string and append it
                # to the growing secret code
                secret_code += str(len(words[line_index]))
            
            else:
                # If the line does not have enough words,
                # add "0" as a placeholder digit
                secret_code += "0"
        
        # After processing all lines in the poem,
        # store the completed secret code
        secret_codes.append(secret_code)
    
    # Return all generated secret codes
    return secret_codes


# Sample poem 1
poem = "Stars and the moon\nshine in the sky\nwhite and bright\nuntil the end of the night"

# Sample poem 2
poem2 = "The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow"

# Sample poem 3
poem3 = "There\nonce\nwas\na\ndragon"

# Call the function with all poems
# and print the resulting secret PIN codes
print(pin_extractor([poem, poem2, poem3]))
