# FizzBuzz Python (With Loops)

# Fizzbuzz solution with while loop and else if statements
i = 1 

while i <= 100:
    if i % 3 == 0 and i % 5 == 0:
        print ("Fizzbuzz")
    elif i % 3 == 0:
        print ("Fizz")
    elif i % 5 == 0:
        print ("Buzz")
    else:
      print (i)
    # increase number by one after checking conditionals
    i += 1

