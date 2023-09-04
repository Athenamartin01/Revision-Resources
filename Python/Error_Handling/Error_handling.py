try: #runs contents and watches for errors
    raise ValueError("invalid value inputted") #raises an error
except(ZeroDivisionError,ValueError): #if either of these errors popup the contents are run
    pass
else: #runs if no exception is found
    pass
finally: #runs this with or without error
    pass

assert 1+1 == 3 #if the statement is false an AssertionError is given
