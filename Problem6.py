


def populateSquaresList():
    squaresList = []
    for number in range(1,101):
        #score = sumOfAllNumbers
        squaresList.append(number**2)
        
    return sum(squaresList)
    
   

def squareOfSums():
    sumsList = []   
    for number in range(1,101):
        sumsList.append(number)
    answer = sum(sumsList)
    return answer**2

print squareOfSums() - populateSquaresList()