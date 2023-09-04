nums = [1,2,3,4,5]

def func_1(x):    
    return(x) #Returns a value and ends the current function.



### We use decorators to 'decorate' functions (adding extra features)
def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

@decor
def print_text():
    print("Hello world!")
print_text()

### We can also call functions within themselves, this is called recursion
def factorial(x):
    if x == 1:
        return 1
    else: 
        return x * factorial(x-1)

double = (lambda x: 2*x)(5) #creates a simple function with x value 5  
    
list(map(double,nums)) #map takes a function and applies it to each value in the list 
list(filter(lambda x: x%2==0, nums)) #filter removes any values which don't hold true to the function 
