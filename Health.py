
##Formula: 703 x weight (lbs) / [height (in)]2


##BMI = int (have user input weight in lbs and height in inches)

Weight = 255
Height = 76

##**Possibly have two call boxes, one for feet and one for inches

#Feet = [User input] / 12 = inches

while True:
    try:
        inches = int(input("Please enter your height in inches to the nearest whole number"))
    except ValueError:
        print ("I'm Sorry, please input a whole number")
        continue
    else:
        #Successfull Input
        break

if inches >0:
    BMI = inches


else:
    print ("Unless you're a ghost, please enter a positive whole number")
BMI = (703 * Weight)/(inches ** 2)
print "Your BMI is " + str(BMI)

