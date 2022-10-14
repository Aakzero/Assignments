1. Write a Python program to convert kilometers to miles?
   a=float(input("Enter a value in kilometer "))
   b=a*0.6214
   print(a,"kilometer is equal to",b,"mile")

2.Write a Python program to convert Celsius to Fahrenheit?
   a=float(input("Enter a value of temperature in degree celsius "))
   b=a*1.8+32
   print(a,"degree celsius is equal to",b,"fahrenheit")

3.Write a Python program to display calendar?
   import calendar as cal
   a=int(input("Enter the year of calendar which you wish to see "))
   print(cal.calendar(a))

4.Write a Python program to solve quadratic equation?

   import math

   a = float(input("Enter a value for coeffifient 'a' "))
   b = float(input("Enter a value for coeffifient 'b' "))
   c = float(input("Enter a value for coeffifient 'c' "))

   q = b * b - 4 * a * c
   if q > 0:
       e = math.sqrt(q)
       w = 2 * a
       x1 = (-b + e) / w
       x2 = (-b - e) / w
       print("The root of the equation are \n", "First root", x1, "\nSecond root", x2)
   else:
       r1 = -q
       r2=math.sqrt(r1)
       t = -b / (2 * a)
       y = r2 / (2 * a)
       print("The roots of the equation are \n""First root=", t, "+", y, "i""\nSecond root=", t, "-", y, "i")

5.Write a Python program to swap two variables without temp variable?
   l=[]
   a=input("Enter a number to put it in variable a ")
   b=input("Enter a string to put it in variable b ")
   l.append(a)
   l.append(b)
   b=l[0]
   a=l[1]
   print("variable a=",a,"\nvariable b=",b)

