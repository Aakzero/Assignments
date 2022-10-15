1.Write a Python Program to Find the Factorial of a Number?
   try:
       a = int(input("Enter a number "))
       x = 1
       if a == 0:
           print("The factorial of the number is 1")
       elif a < 0:
           print("Factorial of a negative number does not exist")
       else:
           while a > 0:
               x = x * (a)
               a = a - 1
           print("The factorial of the number is", x)
   except:
       print("Enter only an integer")

2.Write a Python Program to Display the multiplication Table?
   try:
       a = int(input("Enter an integer to see its table "))
       for i in range(1,11):
           x= a*i
           print(a,"x",i,"=",x)
   except:
       print("Enter an integer only")

3. Write a Python Program to Print the Fibonacci sequence?
   try:
       q=int(input("Enter a number upto to which you wish to see the fibonacci series"))
       a=0
       c=0
       z=0
       i=0
       while z<q:
          print(c)
          c=a+i
          if c==1:
              i=1
          if c==0:
              c=1
          a=i
          i=c
          z=z+1
   except:
       print("Enter only an integer")

4.Write a Python Program to Check Armstrong Number?
   try:
      a=input("Enter a number to check wheather it is an armstrong number ")
      if type(int(a))==int:
       p = int(a)
       x = 0
       q=len(a)
       l=[]
       for i in range(0,q):
           d=int(a)%10
           l.append(d)
           a=int(a)/10
           x=x+l[i]*l[i]*l[i]
       if x==p:
        print(p,"is an armstrong number")
       else:
        print(p,"is not an armstrong number")
   except:
       print("Enter only an integer")

5. Write a Python Program to Find Armstrong Number in an Interval?
   try:
       k,l=input("Enter an interval to print the armstrong numbers between them ").split()
       for a in range(int(k),int(l)+1):
             p = int(a)
             x = 0
             q = len(str(a))
             l = []
             for i in range(0, q):
               d = int(a) % 10
               l.append(d)
               a = int(a) / 10
               x = x + l[i] * l[i] * l[i]
             if x == p:
               print(p)
   except:
       print("Enter only an integer interval")

6.Write a Python Program to Find the Sum of Natural Numbers?
   try:
       a=int(input("Enter a natural number to print sum of all natural numbers upto it"))
       x=0
       if a>0:
          for i in range(1,a+1):
            x=x+i
          print(x)
       else:
           print("Enter a number greater than zero")
   except:
       print("Enter a natural number only")

