def pin_extractor(poem):
    secret_code = ""
    lines = poem.split('\n')

    for line_index, line in enumerate(lines):
        print(line_index, line)
        words = line.split()
        secret_code += str(len(words[line_index]))


poem = "Stars and the moon\nshine in the sky\nwhite and bright\nuntil the end of the night"

pin_extractor(poem)
