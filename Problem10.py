def primeChecker(number):
    for x in range(2,((number/2)+1)):
        if number % x == 0:
            return False
    return True  
    
y = []   
for number in range(1,1000):
    if primeChecker(number):
        y.append(number)
totalsum = sum(y)  
print y,totalsum

    
    