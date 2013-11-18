import re
import sys

infile = open(sys.argv[1])
outfile = open(sys.argv[1].rstrip(".csv") + "2" + ".csv", "w")

for line in infile:
	line = line.replace("\t",",")
	outfile.write("," + line)
	
