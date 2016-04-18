# This file was *autogenerated* from the file /Users/LandonDare/Desktop/ellipticCurve/ec_run.sage
from sage.all_cmdline import *   # import sage library
_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_4 = Integer(4); _sage_const_593439483948394349 = Integer(593439483948394349); _sage_const_29579385439865947694694684968492467204765870577p = RealNumber('29579385439865947694694684968492467204765870577.'); _sage_const_32934893483948394 = Integer(32934893483948394); _sage_const_200000000 = Integer(200000000); _sage_const_10000000 = Integer(10000000)#
# Landon Dare 112932095
#
# set up elliptic curve
p = _sage_const_29579385439865947694694684968492467204765870577p 
field = GF(p)
curve = EllipticCurve(GF(p),[_sage_const_32934893483948394 ,_sage_const_593439483948394349 ])



# Read in file for variables
# should be in the form
# e x1 lowest_x2 lowest_y2 
#
path = '/Users/LandonDare/Desktop/ellipticCurve/data.txt'
lines = open(path).read().splitlines()
inputValues = lines[len(lines) -_sage_const_1 ].split(' ')


#set up x1
x1 = int(inputValues[_sage_const_1 ])
startPoint = curve.lift_x(x1)

#set up multiplication
# e is an integer that will determine the number point duplications to find x2
e = int(inputValues[_sage_const_0 ])
testPoint = e * startPoint 

#set up current lowest y2
lowest_x2 = int(inputValues[_sage_const_2 ])
lowest_y2 = int(inputValues[_sage_const_3 ])
lowest_e = int(inputValues[_sage_const_4 ])


print("all values read in as the following:")
print( "\te = " + inputValues[_sage_const_0 ])
print( "\tx1 = " + inputValues[_sage_const_1 ])
print( "\tlowest_x2 = " + inputValues[_sage_const_2 ])
print( "\tlowest_y2 = " + inputValues[_sage_const_3 ])
print( "\tlowest_e = " + inputValues[_sage_const_4 ])

#want ti double the point until we get a low enough y2

# lets gor for 15 million at a time?
# should be able to pick right back up from the file

#can run very fast, almost 5000 a second
runBlock = _sage_const_200000000 
writeBlock = _sage_const_10000000 

while(e < runBlock):
	#test for success
	if(testPoint[_sage_const_1 ] < lowest_y2):
		#if found set the new lowest point
		lowest_x2 = testPoint[_sage_const_0 ]
		lowest_y2 = testPoint[_sage_const_1 ]
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
	if(e % writeBlock == _sage_const_0 ):
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
	e = e + _sage_const_1 
	# use fast point doubling 
	testPoint = testPoint + startPoint


















