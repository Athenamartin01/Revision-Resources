import itertools as it
#Infinite Iterations:
it.count(3,2) #increments by 2 from 3 to infinity unless stopped 
it.cycle("hello") #cycles through lists and strings infinitely 
it.repeat(7,3) #repeats the number 7 3 times or infinitely with no 3 

#Combinatoric Iterators:
it.product("ABCD", repeat=2) #iterates through all of the possibile combinations in the form of tuples
it.permutations("ABCD",2) #iterates through all of the permutations (moving values, not creating or destroying)
it.combinations("ABCD",2) #iterates all combinations (perm but order doesnt matter)
it.combinations_with_replacement("ABCD",2) #combinations but repeat values are allowed
    
#Normal Iterations
it.accumulate(range(8)) #iterates through the cummulative values eg, 1,3,6,10,etc
it.compress("ABCD",[1,0,0,1]) #iterates through "ABCD" only when the list is a 1 eg, AD
it.takewhile(lambda x: x<5, [1,4,6,5,2]) # Iterates values until the statement is True
it.dropwhile(lambda x: x<5, [1,4,6,5,2]) # Iterates from the first value to return True   
it.islice("ABCD",2,None,1) #iterates starting from 2 ending at None with step 1
it.pairwise("ABCD") #iterates through the pairs AB BC CD
it.zip_longest("ABCD","XY", fillvalue=".") #iterates AX,BY,C.,D. as tuples