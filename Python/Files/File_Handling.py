listE = [1,2,3,4]

fileF = open("filename.txt","r+") #opens a file to be read("r") or written("w") to
                                  #r+ does both read and write
cont = fileF.read()  #assigns a variable to the contents of the file
cont = fileF.read(4) #reads the next 4 characters
cont = fileF.readline() #assigns the variable the contents of the next line
fileF.readlines()   #creates a list where each item is a line
    
fileF.write("...") #overwrites a file and all the following text
                       #if assigned to a variable, displays amount of characters
fileF.writelines(listE) #writes each item of a list on a seperate line    

fileF.tell() #returns the current position in the file

fileF.close() #closes the opened file