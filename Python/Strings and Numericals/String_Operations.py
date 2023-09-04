str_1 = "Hello " + "World" #Outputs "Hello World" as 1 string
str_1[0] #Outputs the first character of the string
str_1[6:8:2] #Outputs everything between chr 6 to 8 in a step of 2. 

var_1 = 1
print(f"Variable : {var_1}") #f strings allow variables to be apart of the string
print("{1}{0}{1}".format("cad","abra")) #prints abracadabra
print(",".join(["spam", "eggs", "ham"])) #prints "spam, eggs, ham"
print("Hello ME".replace("ME", "world")) #prints "Hello world"
print("Hello World".count("l")) #prints 3
print("This is a sentence.".startswith("This")) #prints "True"
print("This is a sentence.".endswith("sentence.")) #prints "True"
print("This is a sentence.".upper()) #prints "THIS IS A SENTENCE."
print("AN ALL CAPS SENTENCE".lower()) #prints "an all caps sentence"
print("hello world".capitalize()) #prints " Hello world"
print("hello world".title()) #prints "Hello World"
print("spam, eggs, ham".split(", ")) #prints "['spam', 'eggs', 'ham']"
print("hello   ".rstrip()) #prints "hello", removes leading white space
print("12345".isdigit()) #prints True if the string is made of numbers only
print("Hello".isalpha()) #prints True is the string is made of letters only
print("Hello123".isalnum()) #prints True is string is made of only alphanumeric characters
print("Hello".center(10,"-")) #prints "--Hello--"
print("Hello".ljust(10,"-")) #prints "Hello----"
print("Hello".rjust(10,"-")) #prints "----Hello"