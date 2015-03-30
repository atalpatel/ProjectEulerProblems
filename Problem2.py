def getAnswer():
    first = 1
    middle = 1
    new = 0 
    total = 0 
    while new < 4000000:
        first = middle
        middle = new
        new = first + middle 
        if new % 2 == 0:
            total += new
    print total 