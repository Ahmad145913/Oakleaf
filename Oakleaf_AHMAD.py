#  ahmad_145913
import math
import matplotlib.pyplot as plt


def OakLeafX(teta):  # function that returns Xteta
    # define variables to get a value of Xteta and return it
    a = 0.001 * math.pow(math.cos(teta), 9) * math.pow(math.cos(5 * teta), 10)
    b = 0.25 * math.sin(2 * teta)
    c = 1 - 0.5 * (math.pow(math.sin(10 * teta), 2))
    d = 1 - (math.pow(math.cos(teta) * math.cos(3 * teta), 8))
    Xteta = a + (b * c * d)
    return Xteta


def OakLeafY(teta):  # function that returns Yteta
    # define variables to get a value of Yteta and return it
    e = math.sin(teta)
    f = 0.2 * math.pow(math.sin(10 * teta), 2)
    g = 0.5 + (math.pow(math.sin(2 * teta), 2))
    Yteta = e * (1 - (f * g))
    return Yteta


def generateOakLeaf():  # a function to create the parameters to generate the OakLeaf
    xList = [OakLeafX(math.radians(i)) for i in range(0, 180)]  # list with for loop to fill with elements from Xteta
    yList = [OakLeafY(math.radians(i)) for i in range(0, 180)]  # list with for loop to fill with elements from Yteta
    return xList, yList


def plot(xList, yList, title):  # function for display the shape of OakLeaf using matplotlib library
    plt.plot(xList, yList)
    plt.title(title)
    plt.show()


xList, yList = generateOakLeaf()
plot(xList, yList, "One Oak Leaf")  # display the oakleaf with specific parameters


def generateRotatedList(xList, yList, angle):  # a function to rotate the points(xList,yList)
    xRotatedList = [yList[i] * math.sin(math.radians(angle)) + xList[i] * math.cos(math.radians(angle)) for i in
                    range(0, 180)]  # List for rotate the point (X)
    yRotatedList = [yList[i] * math.cos(math.radians(angle)) - xList[i] * math.sin(math.radians(angle)) for i in
                    range(0, 180)]  # List for rotate the point (Y)
    return xRotatedList, yRotatedList


def generateOakLeafPattern(rotationAngle):  # a function to get the pattern of the rotation
    xPatternList = []
    yPatternList = []
    xList, yList = generateOakLeaf()
    xPatternList = xList
    yPatternList = yList
    if rotationAngle == 0:  # if condition to avoid (ZeroDivisionError exception)
        count = 1
    else:
        count = int(360 / rotationAngle)
        for j in range(1, count):  # for loop to generate two list to rotate the shape
            xRotatedList, yRotatedList = generateRotatedList(xList, yList, rotationAngle * j)
            xPatternList += xRotatedList
            yPatternList += yRotatedList
    return xPatternList, yPatternList
    

def plotPattern(rotationAngle):  # function used to display the final result of the patterns and its rotation
    firstList, secondList = generateOakLeafPattern(rotationAngle) # lists we will fill accordin to the generateOakLeafPattern() funtion
    plot(firstList, secondList, "Oak Leaf Pattern Angle: " + str(rotationAngle))  # use the function that we already
    # defined to display the final result  after fill it with specific parameters


# display the final result with the angles that you want

plotPattern(0)
plotPattern(180)
plotPattern(90)
plotPattern(45)
plotPattern(15)
