1. The two values of boolean data type are true and false. They are usually used to validate a condition wheather
   it is true or false.

2. The three boolean operators are AND , OR , NOT.

3. Logic table for boolean operator

    Boolean value  And     OR             Boolean Value   Not
    True&True      True    True             True          False
    True&False     False   True             False         True
    False&True     False   True
    False&False    False   False

4. boolean values for following expression
    (5 > 4) and (3 == 5)               = False
    not (5 > 4)                        = False
    (5 > 4) or (3 == 5)                = True
    not ((5 > 4) or (3 == 5))          = False
    (True and True) and (True == False)=False
    (not False) or (not True)          =True

5.The six comparison operators are <, >, >=, ==, <=, !=

6. Equal to operator is used to check a condition (==)
   Asignment operator is used to assign a value to variable (=)

   example for equal to operator:
                 if a==6
                     print("the value of a is 6")
                 else:
                     print("value of a is not 6")
                 # here "==" is used to check wheather a == 6.

   example for assignment operator:
                 a = b+c
                 #here we are assigning the result of a+b to a.

7.  spam = 0
    1.if spam == 10:
    2.  print(eggs)
    3.if spam > 5:
    4.   print(bacon)
    5.else:
    6.   print(ham)
    7.   print(spam)
    8.   print(spam)

   Here the first block is from line 1 to 2, second block is from line 3 to 4 and third block is from line 5 to 8

8.Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints
Greetings! if anything else is stored in spam.

    a=input("enter a number")
    spam=int(a)
    if spam == 1:
        print("Hello")
    elif spam == 2:
        print("Howdy")
    else:
        print("Greetings")

9. To stop an infinite loop we need to press 'CTRL+C'


10. Break statement will terminate that particular loop at once and will execute the code outside that loop, whereas
    continue statement will iterate that loop again while skipping the code after continue.

11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

   There is no difference between range(10), range(0,10), range(0,10,1) as default start is 0, default step is 1.


12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
program that prints the numbers 1 to 10 using a while loop.

    #printing 1 to 10 using FOR loop
    for a in range(1,11):
        print(a)

    #printing 1 to 10 using WHILE loop
     a=1
     while a<11 :
         print(a)
         a=a+1

13.If you had a function named bacon() inside a module named spam, how would you call it after
importing spam?

   #calling bacon() after importing spam
     spam.bacon()


