#BUG: {An error in a program that prevents the program from running as expected.}
#Function: {A piece of code that you can easily call over and over again.}
#Loop: {The action of doing something over and over again.}


#Data Types: 
1) PEMDAS
2) SYMBOLS
3) Input Functions

1) #Rules PEMDAS priorities
(P) Parenthesis - (a)
(E) Exponential - (a**b)
(M) Multiplication - (a*b)
(D) Division - (a/b)
(A) Additional - (a+b)
(S) Subtraction - (a-b) 

Modulus - (a%b)

2) #SYMBOLS
Equal to - (a==b)
Not equal to - (a!=b) or (a<>b)
Greater than - (a>b)
Greater than or equal to  - (a>=b)
Lesser than - (a<b)
Lesser than or equal to - (a<=b)
Assigning - (a=b)

3) #Input Functions
String - ("Hello World")

Concatenate - ("Hello" + "World")

Subscript - print("Hello"[0])
  output: ("H") #Count at position 0 first, not position 1
    
Interger - (123 + 456)
  output: (123456) 
    
Float - ("3.14159") #Decimal is a float

Str - num_char = len(input("What is your name?"))
#Input bowen
      new_num_char = str(num_char)
#5
      print("Your name has" + new_num_char + "characters")
  output: (Your name has 5 characters)

Doc String - """ (insert) """ #Comments 

#TKinter 
4) #Arguments with default values
def my_functions(a = 1, b = 2, c = 3):
  #do this with a
  #then do this with b
  #finally do this with C
excute my_function()

#unlimited Arguments output as tuple 
default setting been taught:
def add(n1, n2):
  return n1 + n2

but if to add more arguments: 
def add(*args):
  for n in args:
    print(n)

#then to sum it:
  #*agrs packed all the input number
def add(*agrs): 
  sum = 0 
  for n in args:
    sum += n
  return sum

#Example of **kwargs:
def calculate (n, **kwargs): 
  print(kwargs) 
  n += kwargs["add]
  n *= kwargs["multiply"]
  print(n)
calculate(n, add = 3, multiply = 5)
               
