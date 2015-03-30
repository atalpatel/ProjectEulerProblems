def palNumber():
    numberpal = 0 
    for x in range(100,1000):
        for y in range(100,1000):
            multiple = str(x * y)
            if multiple[::1] == multiple[::-1]:
                print max(multiple)
                #if numberpal < multiple:
                 #   numberpal = multiple
                  #  print numberpal 
        