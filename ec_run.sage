#
# Landon Dare 112932095
#
# set up elliptic curve
p = 29579385439865947694694684968492467204765870577.
field = GF(p)
curve = EllipticCurve(GF(p),[32934893483948394,593439483948394349])



# Read in file for variables
# should be in the form
# e x1 lowest_x2 lowest_y2 
#
path = '/home/landondare/EllipticCurve/data.txt'
lines = open(path).read().splitlines()
inputValues = lines[len(lines) -1].split(' ')


#set up x1
x1 = int(inputValues[1])
startPoint = curve.lift_x(x1)

#set up multiplication
# e is an integer that will determine the number point duplications to find x2
e = int(inputValues[0])
testPoint = e * startPoint 

#set up current lowest y2
lowest_x2 = int(inputValues[2])
lowest_y2 = int(inputValues[3])
lowest_e = int(inputValues[4])


print("all values read in as the following:")
print( "\te = " + inputValues[0])
print( "\tx1 = " + inputValues[1])
print( "\tlowest_x2 = " + inputValues[2])
print( "\tlowest_y2 = " + inputValues[3])
print( "\tlowest_e = " + inputValues[4])

#want ti double the point until we get a low enough y2

# lets gor for 15 million at a time?
# should be able to pick right back up from the file

#can run very fast, almost 5000 a second
runBlock = 2000000000
writeBlock = 100000000

while(e < runBlock):
	#test for success
	if(testPoint[1] < lowest_y2):
		#if found set the new lowest point
		lowest_x2 = testPoint[0]
		lowest_y2 = testPoint[1]
		lowest_e = e
		#print to the console
		print("!!!!!!!found new y2")
		print(str(testPoint))
		print(str(e))
		#print to file
		with open(path, "a") as dataFile:
		    dataFile.write("\n\n!!!!!!!!!!!!!!!!!! NEW LOWEST FOUND " + str(e) + " !!!!!!!!!!!!!!!!!!\n")
		    dataFile.write(str(e) + " ")
		    dataFile.write(str(x1) + " ")
		    dataFile.write(str(lowest_x2) + " ")
		    dataFile.write(str(lowest_y2) + " ")
		    dataFile.write(str(lowest_e))
		    dataFile.close()

	# status block to let me know its still running
	if(e % writeBlock == 0):
		with open(path, "a") as dataFile:
		    dataFile.write("\n\n/////////////////// Block " + str(e) + " /////////////////////////\n")
		    dataFile.write(str(e) + " ")
		    dataFile.write(str(x1) + " ")
		    dataFile.write(str(lowest_x2) + " ")
		    dataFile.write(str(lowest_y2) + " ")
		    dataFile.write(str(lowest_e))
		    dataFile.close()
	#
	#Increment stage
	e = e + 1
	# use fast point doubling 
	testPoint = testPoint + startPoint



















