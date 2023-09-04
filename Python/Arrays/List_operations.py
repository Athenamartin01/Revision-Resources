Int1 = 1
def Function():
    pass

listE = [1,2,3,4,5] #creates a list of 5 items from 1 to 5
listF = listE[0:4:2] #makes a new list of items 0 to 3 in listE with step 2
listG = [i**2 for i in range(9) if i%2 == 0] #creates a list of i**2 for i in range 9 if i is even 

if 1 in listE: #checks to see if 1 is in the list
    pass
if all([i > 5 for i in listE]): #only runs the code if all items are under 5
    pass
if any([i % 2 == 0 for i in listE]): #only runs the code if there's an even item
    pass

for v in enumerate(listE): #runs with v being (i,nums[i])
    pass

list(range(5,10,2)) #creates a list of values 
listE.count(1) #Counts the amount of 1's in the list
listE.append(6) #adds item 6 to the end of the list
listE.extend(listF)#Used for append each value from an iterable
listE.insert(0,10) # inserts 10 into th first position
listE.remove(Int1) #removes the first instance of the value in the list
listE.sort() #sorts the list from lowest to highest value
listE.sort(reverse = True) #sorts highest to lowest
listE.reverse() #Reverses List
sorted(listE, key=Function) # sorts the list, via the functions return values 
zip(listE,listF) #creates a list of tuples of (listE[i],listF[i])
