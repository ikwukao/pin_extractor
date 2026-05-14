def pin_extractor(poem):
    secret_code = ""
    lines = poem.split('\n')

    for line_index, line in enumerate(lines):
        print(line_index, line)


poem = "Stars and the moon\nshine in the sky\nwhite and bright\nuntil the end of the night"

pin_extractor(poem)
