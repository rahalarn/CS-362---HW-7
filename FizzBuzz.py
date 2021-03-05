def fizz():
   num = 2
   res = "1"
   for i in range(99):
      if num % 3 == 0 and num % 5 == 0:    
         res += (" " + str(num))
      elif num % 3 == 0:
         res += " Fizz"
      elif num % 5 == 0:
         res += " Buzz"
      else:
         res += (" " + str(num))
      num += 1
   return res

def fizzbuzz():
   num = 2
   res = "1"
   for i in range(99):
      if num % 3 == 0 and num % 5 == 0:    
         res += " FizzBuzz"
      elif num % 3 == 0:
         res += " Fizz"
      elif num % 5 == 0:
         res += " Buzz"
      else:
         res += (" " + str(num))
      num += 1
   return res

