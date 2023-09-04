import sys

for line in sys.stdin: #Gets inputs from the user 
    sys.stdout.write(line) #Outputs the variable 'line'
    print(line, file = sys.stderr) #outputs 'line' as an error