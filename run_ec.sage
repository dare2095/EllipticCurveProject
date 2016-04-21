#
# Landon Dare 112932095
#
# set up elliptic curve
p = 29579385439865947694694684968492467204765870577.
field = GF(p)
curve = EllipticCurve(GF(p),[32934893483948394,593439483948394349])

idNumber = 12932095


# Read in file for variables
# read from the top
path = '/home/landondare/EllipticCurveProject/data.txt'
lines = open(path).read().splitlines()
inputValues = lines[0].split(' ')

x2 = int(inputValues[0])
y2 = int(inputValues[1])
f = int(inputValues[2])
finalF = 0

startPoint = curve.lift_x(x2)
testPoint = f * startPoint


block = 100000000
found = False

print("\n\n///////////// BEGIN /////////////////////")
print(" entering loop with start Point : " + str(startPoint))
while found == False:
	while f < block:
		if(int(testPoint[0]) % 100000000 == idNumber):
			print("FOUND IT YALL")
			print(str(testPoint))
			print(str(f))
			#print to file
			with open(path, "a") as dataFile:
			    dataFile.write("\n\n!!!!!!!!!!!!!!!!!!FOUND " + str(f) + " !!!!!!!!!!!!!!!!!!\n")
			    dataFile.write(str(f) + " ")
			    dataFile.write(str(testPoint))
			    dataFile.close()
			    finalF=f
			    f=1000000010
			    found = True
		if(f % 5000000 == 0):
			print("still running at f : " + str(f))
			with open(path, "a") as dataFile:
			    dataFile.write("\n\n################### Block is still running" + str(f) + " ####################\n")
			    dataFile.write(str(f) + " ")
			    dataFile.write(str(testPoint))
			    dataFile.close()

		f += 1
		testPoint = testPoint + startPoint
	block = block + 100000000






