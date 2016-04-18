#path = '/home/landondare/ellipticCurve/data.txt'
#/Users/LandonDare/Desktop
path = '/Users/LandonDare/Desktop/ellipticCurve/data.txt'
lines = open(path).read().splitlines()
inputValues = lines[len(lines) -1].split(' ')

print(lines)
print( "e = " + inputValues[0])
print( "x1 = " + inputValues[1])
print( "lowest_x2 = " + inputValues[2])
print( "lowest_y2 = " + inputValues[3])
print( "lowest_e = " + inputValues[4])

e = int(inputValues[0])
x1 = int(inputValues[1])
lowest_x2 = int(inputValues[2])
lowest_y2 = int(inputValues[3])
lowest_e = int(inputValues[4])

e = e+1

with open(path, "a") as dataFile:
    dataFile.write("\n\n/////////////////// Block " + str(e) + " /////////////////////////\n")
    dataFile.write(str(e) + " ")
    dataFile.write(str(x1) + " ")
    dataFile.write(str(lowest_x2) + " ")
    dataFile.write(str(lowest_y2) + " ")
    dataFile.write(str(lowest_e))
    dataFile.close()



