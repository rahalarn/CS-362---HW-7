def leap_year(num):
   if (int(num) % 4 == 0) and (int(num) % 100 != 0):
      return True
   else:
      return False
