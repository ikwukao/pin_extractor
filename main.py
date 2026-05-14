def pin_extractor(poem):
    secret_code = ""
    lines = poem.split('\n')

    for line in lines:
        print(line) 


poem = """ 
        Stars and the moon\n
        shine in the sky\n
        white and bright\n
        until the end of the night 
       """

pin_extractor(poem)
