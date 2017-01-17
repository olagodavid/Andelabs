"""Create a function fizzBuzz to return 'Fizz', 'Buzz', 'FizzBuzz', or the argument it receives, 
all depending on the argument of the function, a number that is divisible by, 3, 5, or both 3 and 5, respectively.
When the number is not divisible by 3 or 5, the number itself should be returned.
"""
"""FIZZBUZZ"""

def fizz_buzz(number):
  
  if number%15 == 0: 
    return "FizzBuzz"

  elif number%3==0:
    return "Fizz"

  elif number%5==0:
    return "Buzz"

  else:
    return number
