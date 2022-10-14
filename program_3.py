1. Write a Python Program to Check if a Number is Positive, Negative or Zero?

   try:
       a = float(input("Enter a number "))
       if a==0:
         print("Entered number is zero")
       elif a>0:
         print("Entered number is positive")
       else :
         print("Entered number is negative")
   except:
       print("You must enter a number only")

2.Write a Python Program to Check if a Number is Odd or Even?
   try:
       a = input("Enter an integer number ")
       if float(a) == float(0):
           print("Entered number is zero")
       elif int(a) == 0:
           print("Entered number is zero")
       elif int(a) % 2 == 1:
           print("Entered number is a odd number")
       elif int(a) % 2 == 0:
           print("Entered number is an even number")
   except:
       try:
          if type(float(a)) == float:
               print("You have entered a floating number please enter only integer")
       except:
           print("You must enter only an integer")

3.Write a Python Program to Check Leap Year?
   try:
       a = int(input("Enter a year "))
       if a % 4 == 0:
           print("Entered year is a leap year")
       else:
           print("Entered year is not a leap year")
   except:
       print("Please enter a valid year")
4.Write a Python Program to Check Prime Number?
   try:
       a=int(input("enter a number"))
       z=0
       for i in range(2,a):
          if a%i==0:
              z=1
       if z==0:
          print("Entered number is prime number")
       else:
           print("Entered number is not a prime number")
   except:
       print("Enter an integer")

5.Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
   s=[2]   #2 is the only even prime number
   z = 0
   for a in range(3,10000):
       for i in range(2, a):
           if a % i == 0:
                z=1
                break
       if z==0:
           s.append(a)
       else:
           z=0
   print(s)







