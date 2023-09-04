import random as rng

Num1,Num2,Num3 = 1,2,3
Int1,Int2 = 4,5
Lst1 = [6,7,8]
Low,High,Mode = 1,100,5
alpha,beta,mu,sigma = 0.9,0.8,0.7,0.6


#Integer Random Operators
rng.randrange(Num1,Num2,Num3) #Randomly selects a number in range (Start,Stop,Step)
rng.randint(Int1,Int2) #Selects an integer between 1 and 10
rng.random(Num1,Num2) #Returns Random float in range

#List Random Operators
rng.choice(Lst1) #Returns random element from list
rng.shuffle(Lst1) #Shuffles List
    
#Distribution Operators
rng.uniform(Num1,Num2) #Return a value from the uniform distribution
rng.triangular(Low,High,Mode) #Return a value from the uniform triangle
rng.betavariate(alpha,beta) #Return a value from the beta distribution
rng.expovariate(alpha) #Return a value from the exponential distribution
rng.gammavariate(alpha,beta) #Return a value from the gamma distribution
rng.gauss(mu,sigma) #Return a value from the normal distribution
rng.lognormvariate(mu,sigma) #Return a value from the log normal distribution
