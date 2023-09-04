ages = {"Alfie":20, "Jasmine":20, "Tom":32} #Dictionary variable type

ages["Alfie"] #Returns the value associated (20)
ages.get("Jasmine", "...") #Returns value associated or returns "..."  by default
ages["Athena"] = 22 #Adds a new variable to the dictionary
ages.pop("Tom") #Removes the key and value

ages.update(ages) #adds the key value pairs from ages to ages 
ages.keys() #gives a readable output for all the keys in a dictionary
ages.values() #gives a readable output for all values
ages.items() #gives readable output for keys and values