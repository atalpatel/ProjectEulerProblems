def distinctPowers():
    y = []
    for a in range(2,101):
        for b in range(2,101):
            multiple = a**b
            while y.count(multiple) < 1:
                y.append(multiple)
                list.sort(y) 
            
    print len(y) 
        
    