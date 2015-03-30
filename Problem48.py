def selfPowers():
    listOfNumbers = []
    sumOfNumbers = 0 
    for number in range(1,1000):
        powerOfNumber = number ** number
        listOfNumbers.append(powerOfNumber)
        
    print sum(listOfNumbers)
        