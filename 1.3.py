''' Chapter 1
    #3: Enhanced Unit Converter
    The unit conversion program we wrote in this chapter is limited to conversions between kilometers and miles. Try
    extending the program to convert between units of mass (such as kilograms and pounds) and between units of
    temperature (such as Celsius and Fahrenheit).
'''

if __name__ == '__main__':
    while(True):
        unit1 = input("Enter in the name of the first unit you are converting from.")
        unit2 = input("Enter in the name of the second unit you are converting to.")

        try:
            ratio = float(input("Enter in the ratio from %s to %s (The conversion rate)"%(unit1, unit2)))
        except:
            print("Please enter in a valid ratio, restarting the programme.")
            continue

        try:
            quantity1 = float(input("How many units of %s do you have?" % unit1))
        except:
            print("Please enter in a legit quantity, restarting the programme...")
            continue

        print("A quantity of %f %s is equal to %f of quantity %s" %(quantity1, unit1, quantity1/ratio, unit2))
        break
