
        
#def triNumbers():  
y = []               
for n in range(1,10000000):
    x = ((n**2)+n)/(2)
    y.append(x)
#print y 
    
    
#def factors():
#    count = 1
#    for number in range(1,y):
#        if number % number == 0:
 #           print number
  #          count += 1
   #             print number 
    #        return False
    
for number in y:
    count = 1
    if number % number == 0:
        print number 
        count +=1
        if count == 500:
            print "True"
         
def factors(y):
    for i in range(1,y):
        if x % i == 0:
            print i 