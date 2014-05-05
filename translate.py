##########################################################
## Rehman, Aali 
## Chan, Jose V
## May 6, 2014
## Final Project
## CPSC 323 TuTh 4:00 - 5:15 PM
#########################################################

## Translate - Compiles the successfully build program
##  into python. (finalv3.py)
def Translate(filename):
    line = []
    filename = open(filename)
    line = filename.readlines()
    filename.close()
    filename = open('finalv3.py', 'w')
    filename.write("""if __name__ == "__main__":""")
    ## Since python doesn't need to declare datatype for variables
    ##  the program automatically jump to BEGIN and skips VARS
    for i in range(4, len(line)):
	    line[i] = line[i].strip()
	    ## Python doesn't requre semicolons
	    line[i] = line[i].replace(';','')
	    ## Change writeln( to print(
	    if line[i].find("writeln(") > -1:
		    line[i] = line[i].replace("writeln(","print(")
		    filename.write('\n\t{}'.format(line[i]))
	    elif line[i] != 'END.':
            ## Write all lines to file. Stop before END. is reached
		    filename.write('\n\t{}'.format(line[i]))
    filename.close()
## END Translate
