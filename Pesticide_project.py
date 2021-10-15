# Break down into dilutions, ratio, volume and dosage

##Dilutions


def dilute():       ########################################################################## what about when you already have a starting amount?

    print("""A dilution is when you decrease the concentration of solute in solution.
    This can be applied in insecticide work to make large batches of spray mix from small very concentrated bottles of pesticide.
    In order to perform a dilution, exactly one missing value mus be present. Let us start
    """) 

    c1 = float(input(
        "Please enter the percent concentration of the concentrate (if unknown , please put 0) "))
    v1 = float(input(
        "Please input the volume of concentrate used in mL (if unknown , please put 0) "))
    c2 = float(input(
        "Please enter the final percent concentration of the spray mix that you'd like to make (if unknown , please put 0) "))
    v2 = float(input(
        "Please enter the total volume that you'd like to make in mL (if unknown , please put 0) "))

    l = [c1,v1,c2,v2]
    i = 0
    n = 0
    while i < len(l):
        if l[i] == 0:
            n += 1
        i += 1
    if n >= 2:
        return "A maximum of one missing value can be used to perform a dilution calculation. Perhaps a ratio calculation is more suitable"
    elif c1 != 0 and c2 != 0 and v1 != 0 and v2 != 0:
        return "There has to be one value missing in order to perform a dilution calculation!"  
    elif c1 == 0:
        c1 = (c2 * v2) / v1
        return "The initial percent concentration of concentrate used to make the spray mix of volume {}mL is {}%".format(int(v2), c1)
    elif v1 == 0:
        v1 = (c2 * v2) / c1
        return "The initial volume of concentrate used to make the spray mix of volume {}mL is {}mL".format(int(v2),v1)
    elif c2 == 0:
        c2 = (c1 * v1) / v2
        return "The final concentration of the spray mix will be {}%".format(c2)
    else:
        v2 = (c1 * v1) / c2
        return "The final volume of the spray mix will be {}mL".format(v2)


##ratios

def ratio():
    print("""
    Ratios can be used in pesticide work when given instructions on how much pesticide to mix with water and you want to figure out how much concentrate to mix with water.
    let us start
    """)

    c1 = float(input("Please enter how much pesticide you are told to mix with water (if given in parts, please give the number of parts): "))
    v1 = float(input("Please enter how much water (in mL) you are told to mix with the pesticide (if given in parts, please give the number of parts): "))
    v2 = float(input("Please enter how much spray mix (in mL) you want to make in total: "))

    c2 = (c1 / v1) * v2

    v3 = v2 - c2

    return "You need to mix {}mL of concentrate with {}mL of water to acquire a total spray mix volume {}".format(c2,v3,v2)

    

###volume

def volume():
    print("""
    Volume can be used in pesticide work to find out how much necessary pesticide is required for a particular area. 
    Let us start, Please choose the shape of the building you are trying to find the volume for.
    """)

    shape = int(input("""
            Enter 1 for square / rectangle, 2 for triangle, 3 for cube / cubic rectangle, 4 for building with peaked roof, 
            5 for circle or 6 for cylindrical silo.
            """))

    def square():
        l = int(input("Please enter the length of the square / rectangle you are working with in meters "))
        w = int(input("Please enter the width of the square / rectangle you are working with in meters "))
        v = (l*w)
        return "The final volume of the square / rectangle is {}m ".format(v)

    def triangle():
        b = int(input("Please enter the length of the base of the triangle in meters "))
        h = int(input("Please enter the length of the height of the triangle in meters "))
        v = (b*h) / 2
        return "The final volume of the triangle is {}m ".format(v)

    def cube():
        l = int(input("Please enter the length of the cube / cubic rectangle you are working with in meters "))
        w = int(input("Please enter the width of the cube / cubic rectangle you are working with in meters "))
        h = int(input("Please enter the height of the cube / cubic rectangle you are working with in meters "))
        v = (l*w*h)
        return "The final volume of the cube / cubic rectangle is {}m ".format(v) 

    def peak():
        l = int(input("Please enter the length of the building with the peaked roof in meters "))
        w = int(input("Please enter the width of the building with the peaked roof in meters "))
        h1 = int(input("Please enter the height of the building with the peaked roof in meters "))
        h2 = int(input("Please enter the height from the ground to the end of the wall (before the peak) in meters "))
        while h2 >= h1:
            print("It is not possible for the height from the ground to the end of the wall to be greater than or equal to height before the peak! ")
            h2 = float(input("Please input a new value for the height to the end of the wall before the peak ")) 
        v1 = (l*w*h2)
        v2 = (l*w*(h1-h2)) / 2
        return "The final volume of the building with the peaked roof is {}m ".format((v1+v2))

    def circle():
        r = int(input("Please enter the radius of the circle you are working with in meters "))
        v = (3.14159265 * r * r)
        return "The final volume of the circle is {}m ".format(v)
    
    def silo():
        r = int(input("Please enter the radius of the silo you are working with in meters "))
        h = int(input("Please enter the height of the silo you are workign with in meters "))
        v = (3.14159265 * r * r * h)
        return "The final volume of the clyndrical silo is {}m ".format(v)
    
    d = {
        1:square, 2:triangle, 3:cube, 4:peak, 5:circle, 6:silo 
    }

    return d[shape]()


#dosage


def dosage():
    print("""
    Dosage calculations can be useful in determining how much spray mix you need for given a volume. As well, it can help with determining how long your fogger machine may take
    """)

    buildingVolume = input("""
    Do you know the volume of the building you are working with? If so, please input the volume in metres. If not, please input 'no' to go to the volume finder tool
    """)
    if buildingVolume == "no":
        return volume()
    else:
        print("Wonderful, let's find the Spray mix you need for the given volume! ")
        buildingVolume = float(buildingVolume)
        print("Please complete the following: I need __ mL of spray mix per __ m3")
        s = float(input("I need __ mL "))
        v2 = float(input ( "For every __ m3 "))

        sprayMixNeeded = (buildingVolume / v2) * s

        print("You will need a total of {}mL of spray mix to spray the entire building".format(sprayMixNeeded))

        proceed = input("Would you like to determine the time required to fog the building? (yes / no) ")
        if proceed == "yes":
            rateOfDispense = float(input("Please input the dispense rate of the fogger machine in mL per minute "))
            timeRequired = (sprayMixNeeded / rateOfDispense)
            return("It will take a total {} minutes to spray {}mL at a rate of {}mL per minute".format(timeRequired, sprayMixNeeded, rateOfDispense))
        else:
            return("As you wish. Remember, you can always find the time required per given spray mix volume using the flowRate tool! ")

#flow rate

def flowRate():
    print("""
    This dosage calculation will help in determining how long it may take to spray the building you're working with.
    """)

    sprayMixNeeded = (input("Do you know the amount of spray mix (in mL) you require to fog your building? If so, please input that number in mL. If not, type 'no' "))
    if sprayMixNeeded == "no":
        return(dosage())
    else:
        sprayMixNeeded = float(sprayMixNeeded)
        rateOfDispense = float(input("Please input the dispense rate of the fogger machine in mL per minute "))
        timeRequired = (sprayMixNeeded / rateOfDispense)
        return("It will take a total {} minutes to spray {}mL at a rate of {}mL per minute".format(timeRequired, sprayMixNeeded, rateOfDispense))


print(dosage())



## Can make an actor class "BuildingToBeWorkedOn" and a utility "Calculations" Class with static methods to be called.

##In this utility class you could have a method just for volume. Start the program by asking the user what they'd like to do. If they choose anything that
##requires volume, ask them for volume, or if they don't know it to input the building shape and dimensions and we can calculate the volume and proceed.