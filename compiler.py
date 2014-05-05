##########################################################
## Rehman, Aali 
## Chan, Jose V
## May 6, 2014
## Final Project
## CPSC 323 TuTh 4:00 - 5:15 PM
#########################################################
import adjust
import translate
import build

if __name__ == "__main__":
    ## Adjust spacing, delete comments
    filename = 'finalv1.txt'
    adjust.Adjust(filename)

    ## Check for errors, and check if program is valid
    ## Return true if valid, false if invalid
    filename = 'finalv2.txt'
    success = build.Build(filename)
    
    ## If build was successful, output "Build Successful"
    ## and convert to python code
    ## If build was unsuccessful, output message
    if success == True:
        print('Build Successful')
        translate.Translate(filename)
    else:
        print('Build Error')
## END main
