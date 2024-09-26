# IT5016
Hello below, I hope to have provided all the labs/functions I was tasked with creating during my studies; hopefully I didn't miss any tasks/labs. If I have, I am sorry.Week 1 to my memory didn't have any coding tasks as it was an introduction to the class and getting everything setup.Week 2—Week 7 should have all the codes and functions.I have split all the codes into files and named them from 1 to 15. I have very basic docstrings explaining my basic understanding of what the task is supposed to complete.I have provided more details on the codes/functions that required more explanation.
For my self-codes, I decided to work on some basic calculators. The first calculator is one I was able to create myself. 

I will start from the top of the code and explain on the way down.
Starting from the top of the file, we have the docstring to explain.What the function is and what task it's supposed to complete. Following that, we have author + any other extra information on the code. Coming to the first actual line of code, we have a function/def. Creating a function starts with using the keyword def followed by the name of the function. * Example: def calculator(): * After we have established the function name, we print two basic messages for the user to read, for example, print (Welcome to the Basic Calculator!").  It is important for these lines of code to be placed at the top of the code block so as to run them at the beginning of the function. Following that, we have our firstuser input function, user input functions are used to take inputs/values from the user with a basic prompt message like, "Input value" * example num1 = float(input("Enter first number:")) * The data that we get from the user should be converted to a float, as a float allows decimal values, not just whole values. The resulting float is assigned to the variable num1, which later can be used in the program for calculations or other operations. A basic TLDR is a line that collects code, converts code, and stores code in variable num1.

Moving onto the if elif and else statements, these are honestly self-explanatory, but I'll give a basic explanation of them to my understanding. Starting with the if statement, the if statement checks a condition; if said condition is true, the code block under it will execute. In the example I have provided below, if the value of age is 18, the code will execute and print the message "You are an adult. This is a super simple statment since it only has to check one condition, moving into the elif statment short for else if. This statment checks another condition if the previous if condition was false. For example, since the age is only equal to 16, it will fail the first if condition and complete the first elif condition and display "You are a teenager." You can also use the else statement at the end to handle all other cases. If none of the previous conditions are true, I'll wrap this up with a final explanation on greater than, less than, and equal to; these are represented by the comparison operators *> greater than*, *< less than*, and *equal ==*. Starting with greater than, the 

first example is a basic greater than if statement since the age is > greater than or = equal to we complete the first statement; the second example is showing a less than elif statement in use since the age = 16; it fails the first statement and moves on to the less than elif statement; the final operator is ==. I don't have an example written down here, but I used it a lot in my actual calculator. The basic explanation of equal is comparing two values; if the values are the same, it evaluates to true if they are not false. 
I have just noticed I should have used real examples from my calculator, but I kind of forgot and just used what I was comfortable with for examples.



example age = 18                             age = 16                                age =10
if age >= 18:                                if age >=18:                            if age >= 18:
    print("You are an adult.") *                 print("You are an adult.")             print("You are an adult,") 
                                             elif age >= 13:                         elif age >= 13:
                                                 print("You are a teen.")           print("You are a teen.")
                                                                                     else:
                                                                                        print("You are a kid.")    




