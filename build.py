##########################################################
## Rehman, Aali 
## Chan, Jose V
## May 6, 2014
## Final Project
## CPSC 323 TuTh 4:00 - 5:15 PM
##########################################################

## RowValue - Returns the row value of a specific non terminal state in the table
def RowValue(value):
    if value == 'P':
        return 0
    elif value == 'I':
        return 1
    elif value == 'X':
        return 2
    elif value == 'Y':
        return 3
    elif value == 'Z':
        return 4
    elif value == 'DL':
        return 5
    elif value == 'D':
        return 6
    elif value == 'T':
        return 7
    elif value == 'SL':
        return 8
    elif value == 'S':
        return 9
    elif value == 'W':
        return 10
    elif value == 'A':
        return 11
    elif value == 'E':
        return 12
    elif value == 'J':
        return 13
    elif value == 'TM':
        return 14
    elif value == "TM'":
        return 15
    elif value == 'F':
        return 16
    elif value == 'N':
        return 17
    elif value == 'Q':
        return 18
    elif value == 'R':
        return 19
    elif value == 'SG':
        return 20
    elif value == 'DG':
        return 21
    elif value == 'ID':
        return 22
    else:
        return 23
## END RowValue function

## ColumnValue - Return the column value of specific terminal state in table
def ColumnValue(value):
    if value == 'v':
        return 0
    elif value == 'w':
        return 1
    elif value == 'x':
        return 2
    elif value == 'y':
        return 3
    elif value == 'z':
        return 4
    elif value == '0':
        return 5
    elif value == '1':
        return 6
    elif value == '2':
        return 7
    elif value == '3':
        return 8
    elif value == '4':
        return 9
    elif value == '5':
        return 10
    elif value == '6':
        return 11
    elif value == '7':
        return 12
    elif value == '8':
        return 13
    elif value == '9':
        return 14
    elif value == '+':
        return 15
    elif value == '-':
        return 16
    elif value == '*':
        return 17
    elif value == '/':
        return 18
    elif value == '(':
        return 19
    elif value == ')':
        return 20
    elif value == 'writeln(':
        return 21
    elif value == 'INTEGER':
        return 22
    elif value == 'PROGRAM':
        return 23
    elif value == ';':
        return 24
    elif value == ',':
        return 25
    elif value == ':':
        return 26
    elif value == '=':
        return 27
    elif value == 'END.':
        return 28
    elif value == 'VAR':
        return 29
    elif value == 'BEGIN':
        return 30
    else:
        return 31
## END ColumnValue function

## CheckVariables - Goes through all the statements in program and checks to 
##  see if variable exists and is declared in VAR. If it exists continue
##  through the loop, if it doesn't exist return false and display error
def CheckVariables(statementList, variables):
    r = [ '*', '/', '+' '-', ';', '=', 'writeln(', 'writeln', '(', ')' ]
    
    for i in statementList:
        if i not in r:
            if i.isdigit() == False:
                if i not in variables and i != '+':
                    return False    
    return True
## END CheckVariables function

## Build - Goes through each word in file and checks the validity of program by using
##  the given LL(1) Table. Also does error checking. If an error is found it displays
##  the error and returns false.
def Build(filename):

    ## Table with Extra rows and columns that return ERROR variables to specify which errors have occurred
    table = [   
    ## P
    [ None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 
      None, None, None, None, None, None, 'PROGRAM I ; VAR DL BEGIN SL END.', None, None, None, None, None, 
      None, None, None ],
    ## I
    [ 'X Y', 'X Y', 'X Y', 'X Y', 'X Y', None, None, None, None, None, None, None, None, None, None, 
      None, None, None, None, None, None, None, None, None, 'ERROR1', None, None, None, None, None, None, None ],
    ## X
    [ 'ID', 'ID', 'ID', 'ID', 'ID', None, None, None, None, None, None, None, None, None, None, None, None, None, 
      None, None, None, None, None, None, None, None, None, None, 'LAMBDA', None, None, None ],
    ## Y
    [ 'Z Y', 'Z Y', 'Z Y', 'Z Y', 'Z Y', 'Z Y', 'Z Y', 'Z Y', 'Z Y', 'Z Y', 'Z Y', 'Z Y', 'Z Y', 'Z Y', 'Z Y', 
      'LAMBDA', 'LAMBDA', 'LAMBDA', 'LAMBDA', None, 'LAMBDA', 'ERROR1', None, None, 'LAMBDA', 'LAMBDA', 'LAMBDA', 
      'LAMBDA', None, None, None, 'ERROR2' ],
    ## Z
    [ 'ID', 'ID', 'ID', 'ID', 'ID', 'DG', 'DG', 'DG', 'DG', 'DG', 'DG', 'DG', 'DG', 'DG', 'DG', None, None, 
      None, None, None, None, None, None, None, None, None, None, None, None, None, None, None ],
    ## DL
    [ 'D : T', 'D : T', 'D : T', 'D : T', 'D : T', None, None, None, None, None, None, None, None, None, None, 
      None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None ],
    ## D
    [ 'I , D', 'I , D', 'I , D', 'I , D', 'I , D', None, None, None, None, None, None, None, None, None, None, 
      None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None ],
    ## T
    [ None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 
      None, None, None, None, None, 'INTEGER ;', None, None, None, None, None, None, None, None, None ],
    ## SL
    [ 'S SL', 'S SL', 'S SL', 'S SL', 'S SL', None, None, None, None, None, None, None, None, None, None, 
      None, None, None, None, None, None, 'S SL', None, None, None, None, None, None, 'S', None, None, 'ERROR3' ],
    ## S
    [ 'A', 'A', 'A', 'A', 'A', None, None, None, None, None, None, None, None, None, None, None, None, None, None, 
      None, None, 'W', None, None, None, None, None, None, 'LAMBDA', None, None, None ],
    ## W
    [ None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 
      None, None, None, 'writeln( I ) ;', None, None, None, None, None, None, None, None, None, None ],
    ## A
    [ 'I = E ;', 'I = E ;', 'I = E ;', 'I = E ;', 'I = E ;', None, None, None, None, None, None, None, None, None, 
      None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None ],
    ## E
    [ 'TM J', 'TM J', 'TM J', 'TM J', 'TM J', 'TM J', 'TM J', 'TM J', 'TM J', 'TM J', 'TM J', 'TM J', 'TM J', 'TM J', 
      'TM J', 'TM J', 'TM J', None, None, 'TM J', None, None, None, None, None, None, None, None, None, None, None, None ],
    ## J
    [ None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, '+ E', '- E', None, None, 
      None, 'LAMBDA', None, None, None, 'LAMBDA', None, None, None, None, None, None, None ],
    ## TM
    [ "F TM'", "F TM'", "F TM'", "F TM'", "F TM'", "F TM'", "F TM'", "F TM'", "F TM'", "F TM'", "F TM'", "F TM'", "F TM'", 
      "F TM'", "F TM'", "F TM'", "F TM'", None, None, "F TM'", None, None, None, None, None, None, None, None, None, 
      None, None, None ],
    ## TM'
    [ None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 'LAMBDA', 'LAMBDA', 
      "* F TM'", "/ F TM'", None, 'LAMBDA', None, None, None, 'LAMBDA', None, None, 'ERROR1', None, None, None, None ],
    ## F
    [ 'I', 'I', 'I', 'I', 'I', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', None, None, '( E )', None, None, 
      None, None, None, None, None, None, None, None, None, None ],
    ## N
    [ None, None, None, None, None, 'Q R', 'Q R', 'Q R', 'Q R', 'Q R', 'Q R', 'Q R', 'Q R', 'Q R', 'Q R', 'Q R', 'Q R', None, 
      None, None, None, None, None, None, None, None, None, None, None, None, None, None ],
    ## Q
    [ None, None, None, None, None, 'SG DG', 'SG DG', 'SG DG', 'SG DG', 'SG DG', 'SG DG', 'SG DG', 'SG DG', 'SG DG', 'SG DG', 
      'SG DG', 'SG DG', None, None, None, None, None, None, None, 'LAMBDA', None, None, None, None, None, None, None ],
    ## R
    [ 'ERROR1', 'ERROR1', 'ERROR1', 'ERROR1', 'ERROR1', 'DG R', 'DG R', 'DG R', 'DG R', 'DG R', 'DG R', 'DG R', 'DG R', 'DG R', 
      'DG R', 'LAMBDA', 'LAMBDA', 'LAMBDA', 'LAMBDA', None, 'LAMBDA', 'ERROR1', None, None, 'LAMBDA', None, None, None, None, 
      None, None, None ],
    ## SG
    [ None, None, None, None, None, 'LAMBDA', 'LAMBDA', 'LAMBDA', 'LAMBDA', 'LAMBDA', 'LAMBDA', 'LAMBDA', 'LAMBDA', 'LAMBDA', 
      'LAMBDA', '+', '-', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None ],
    ## DG
    [ None, None, None, None, None, '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', None, None, None, None, None, None, 
      None, None, None, None, None, None, None, None, None, None ],
    ## ID
    [ 'v', 'w', 'x', 'y', 'z', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 
      None, None, None, None, None, None, None, None, None, None, None, None ],
    ## ERROR CATCHER
    [ None, None, 'ERRORVAR', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 
      None, None, 'ERROR4', None, None, None, None, None, None, None, 'ERROR1', None, 'ERROR1', None ] ]
    
    variables = [] # Keeps track of declared variables
    reserved = [ 'PROGRAM', 'VAR', 'INTEGER', 'BEGIN', 'END.', 'writeln(', 'writeln' ]
    filename = open(filename)
    sourceCode = list(filename.read().split()) # Reads file word by word and stores into a list called SourceCode
    stack = [ '$', 'P' ] # Beginning stack
    statement = [] # Breaks up unreserved words in sourceCode list character by character 
    currentLine = 0 # keeps track of the current line
    var = False # boolean flag that tells if 
    numberOfVars = 0

    ## FOR LOOP
    ## (1) Goes through each word in file and strips all newline, tab, and return characters
    ## (2) Appends all reserved words to a list called statement
    ## (3) If current word is not a reserved word it is appended to statement list character by character
    ## (4) If current word is in VAR list, it is appended to a list called variables
    ## (5) Checks to see if BEGIN is spelled correctly and exists in program
    ## (6) Checks to see if VAR is spelled correctly and exists in program
    for s in range(len(sourceCode)):
        ## (1)
        sourceCode[s] = sourceCode[s].replace('\t','')
        sourceCode[s] = sourceCode[s].replace('\n','')
        sourceCode[s] = sourceCode[s].replace('\r','')
        
        if sourceCode[s] in reserved:
            ## (2)
            statement.append(sourceCode[s])
        else:
            ## (3)
            for t in range(len(sourceCode[s])):
                statement.append(sourceCode[s][t])
                if sourceCode[s][t] == ';':
                    currentLine += 1
            if var == True:
                ## (4)
                if sourceCode[s] != ',' and sourceCode[s] != ':':
                    variables.append(sourceCode[s])
                    numberOfVars += 1
        
        if sourceCode[s] == 'VAR':
            var = True
        elif sourceCode[s] == ':':
            var = False
        
        ## (5)
        if sourceCode[s] == 'BEGIN':
            checkVars = CheckVariables(sourceCode[s+1:-1], variables)
            if checkVars == False:
                print("ERROR: UNKNOWN IDENTIFIER")
                return False
        
        ## (6) 
        elif currentLine == 1:
            if sourceCode[s+1] != 'VAR':
                print("ERROR: VAR is expected")            
                return False
            currentLine += 1
        
        ## (7)
        if sourceCode[s] == ':':
            if sourceCode[s+1] != 'INTEGER':
                print("ERROR: INTEGER is expected")
                return False
        ## (8)
        if currentLine == 3:
            if sourceCode[s+1] != 'BEGIN':
                print("ERROR: BEGIN is expected")
                return False
            currentLine += 1
    #####################
    ## END of FOR LOOP ##
    #####################
 
    ## Checks to see if PROGRAM is spelled correctly and exists in the program
    if sourceCode[0] != 'PROGRAM':
        print("ERROR: PROGRAM is expected")
        return False
    
    ## Checks to see if END. is spelled correctly and exists in the program
    if sourceCode[len(sourceCode)-1] != 'END.':
        print("ERROR: END. is expected")
        return False

    current = None
    count = 0
    index = 0
    error = [ 'ERROR1' , 'ERROR2', 'ERROR3', 'ERROR4', 'ERRORVAR', None ]
    
    ## WHILE LOOP
    ## (1) Goes through list of reserved words and characters one by one. Checks for errors as well
    ## (2) Pop stack and store popped element into variable current
    ## (3) If current variable is END. that means the end of the program has been reached without error
    ## (4) Use LL(1) Table rules to push elements. Store retrieved items from table in variable pending
    ## (5) If the value of the element in the table does not equal None then we have so far not hit an error
    ##  in the program so we continue by pushing the characters onto the stack
    ## (6) If returned value from table is None then there is an unknown error in the program
    ## (7) If table returns ERROR1, ERROR2, ERROR3, ERROR4, OR ERRORVAR then output the error and return false
    while count <= len(statement):
        ## (2)
        current = stack.pop()
        if current == statement[count]:
            ## (3)
            if current == 'END.':
                return True
            count += 1
        elif current != 'LAMBDA':
            ## (4)
            pending = table[ RowValue(current) ][ ColumnValue(statement[count]) ]
            
            if pending not in error:
                pending = pending.split() # create a list of pending characters
                if ''.join(pending) == 'I,D':
                    numberOfVars -= 1
                    if numberOfVars == 0:
                        pending = 'I'
                if pending != None:    
                    ## (5)
                    index = len(pending)-1
                    while index >= 0:
                        stack.append(pending[index])
                        index -= 1
                else:
                    ## (6)
                    print("UNKNOWN ERROR")
                    return False
            else:
                ## (7)
                if pending == 'ERROR1':
                    print("ERROR: Missing semicolon")
                elif pending == 'ERROR2':
                    print("ERROR: Missing colon")
                elif pending == 'ERROR3':
                    print("ERROR: Missing period")
                elif pending == 'ERROR4':
                    print("ERROR: Missing left parentheses")
                elif pending == 'ERRORVAR':
                    print("ERROR: VAR is expected")
                elif current == ')' and statement[count] == ';':
                    print("Error: Missing right parentheses")
                return False
    ####################
    ## END WHILE LOOP ##
    ####################
