import re
Int1=5

r"spam" #Creates a raw string
r"gr.y" # . matches with any character
r"^gr.y$" # ^ implies what it starts with $ what it ends with
r"[aeiou]" # [] provides a way to match only one of a set of characters
r"[A-Za-z]" # matches a letter of any case
r"[^A-Z]" # ^ inverts the group. matching everything outside of it
r"spam(egg)*" # * allows for zero or more repititions of 'egg'
r"gra(y)+" # + allows one or more repititions
r"ice(-)?cream" # ? allows zero or one repititions 
r"abc{1,5}" # {} allows 1 to 5 repititions
r"gr(a|e)y" # | behaves as an or operator
r"(.+) \1" # \1 matches expression of group number 1
r"\d\s\w" #\d is 1 digit, \s is 1 whitespace, \w is one character
r"\D" #capital versions give the opposite result
r"\A\Z\b" #\A \z anchors beginning and end of string, \b space or special character at start or end of string
Re1 = re.compile(r"H..E..") #used to create an rstring object
Str2 = "H....3"
Str1 = "Hwllo"
m1 = Re1.match(Str2) #see if the start of Str2 matches rStr1 at any point
Re1.search(Str2) #looks to see if rStr1 is anywhere within Str2
Re1.findall(Str2) #Creates a list of all the instances where rStr1 is in Str2
Re1.finditer(Str2) #Returns the amount of times rSrt1 appears in Str2
    
m1.group() #Returns the string matched
m1.start() #Returns the starting position of the first match
m1.end() #Returns the end position of the first match
m1.span() #Returns a tuple of the start and end position of the first match
Re1.sub(Str1,Str2,count=Int1) #Replaces Int1 instances of matches in Str1 with Str2 