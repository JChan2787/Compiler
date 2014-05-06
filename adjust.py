##########################################################
## Rehman, Aali 
## Chan, Jose V
## May 6, 2014
## Final Project
## CPSC 323 TuTh 4:00 - 5:15 PM
#########################################################

## FindStart - returns the line of the beginning of the program
def FindStart(line):
	index = line.find('PROGRAM')
	if index != -1:
		if line[7] != ' ':
			line = line[0:7] + ' ' + line[7:] 
			if line[-1:] == ';':
			    line = line[:-1] + ' ;'
		return True, line
	else:
		return False, line
		
## END FindStart

## RemoveComments - Completely remove all comments from the program
def RemoveComments(line):
	index = 0
	line = list(line)
	comment = False
	
	## WHILE LOOP
	## Goes through line character by character
	## If (* is found then all characters proceeding it are
	## removed from the line until *) is read
	while index < len(line):
		if line[index-1] == '(' and line[index] == '*':
			line[index-1] = ''
			line[index] = ''
			comment = True
		elif line[index-1] == '*' and line[index] == ')':
			line[index-1] = ''
			line[index] = ''
			comment = False
		elif comment == True:
			line[index] = ''
		index += 1
    ## END WHILE LOOP

	return ''.join(line)
## END RemoveComments

## AddSpaceBetweenOperators - Adds a space between operators
def AddSpaceBetweenOperators(line):
    operators = [ '+', '-', '*', '/', '=', '(', ')', ',', ':', ';' ]
    index = 0
    previous = False

    if ''.join(line[0:8]) == 'writeln(':
        line = line[0:8] + ' ' + line[8:]
        index = 8

    line = list(line)
    
    ## WHILE LOOP
    ## Goes through line character by characters and adds a space
    ## before and after a specific character (operators list)
    ## If a space was added to the previous character then a space is not
    ## added before the character
    while index < len(line):
        if line[index] in operators:
            if previous == True and line[index][-1:] != ' ':
                line[index] = line[index] + ' '
            else:
                line[index-1] = line[index-1] + ' '
                line[index] = line[index] + ' '
            previous = True
        else:
            previous = False
       
       ## Adds space between INTEGER and previous letter
        if ''.join(line[index:index+3]) == 'INT':
            if line[index-1] != ': ':
                line[index] = ' ' + line[index]
        index += 1
    ## END WHILE LOOP

    return ''.join(line)
## END AddSpaceBetweenOperators

## Adjust - Go through file line by line to fix necessary spacing
##  and delete comments
## (1) Open file and read line by line into a list called line
## (2) Enter for loop and remove newline, tab, carriage return characters
##  - Remove comments
##  - AddSpacing between operators and variables
##  - Write to file
def Adjust(filename):
    start = False
    line = []
    ## (1)
    filename = open(filename)
    line = filename.readlines()
    filename.close()
    filename = open('finalv2.txt', 'w')
    
    ## FOR LOOP
    ## (1A) Remove special characters
    ## (1B) Remove comments from current line
    ## (1C) Find start of program
    ## (1D) Add spacing between specific characters
    ## (1E) Write current line to file (finalv2.txt)
    for i in range(len(line)):
        ## (1A)
        line[i] = line[i].replace('\t','')
        line[i] = line[i].replace('\n','')
        line[i] = line[i].replace('\r','')
        line[i] = line[i].replace(' ', '')
        ## (1B)
        line[i] = RemoveComments(line[i])
        if start == False:
            ## (1C)
            start, line[i] = FindStart(line[i])
        else:
            ## (1D)
            if line[i] != '':
                line[i] = AddSpaceBetweenOperators(line[i])
        ## (1E)
        if line[i] != '':
            filename.write(line[i])
            filename.write('\n')
    ## END FOR LOOP

    filename.close()
## END Adjust
