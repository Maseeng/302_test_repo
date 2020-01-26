Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #Maseeng Masitha
#24 January 2020
#Python 3.4
#Lecture 4: Revision
>>> #Differnce between '15' and 15
>>> Rapinoe = 15
>>> type (Rapinoe)
<class 'int'>
>>> Rapinoe = '15'
>>> type (Rapinoe)
<class 'str'>
>>> 
>>> float (32) #converts an integer into a float.
32.0
>>> 
>>> #To convert integers into strings
>>> a = str(42) #use str in code
>>> type(a)
<class 'str'>
>>> 3.14149 #to string:
3.14149
>>> str (3.14149)
'3.14149'
>>> 59/60
0.9833333333333333
>>> number = 59
>>> number /60.0
0.9833333333333333
>>> # Mixed expressions in above: integers and strings variables representing integers.
>>> 
>>> #Modules
>>> import math #first step
>>> math.pi #dot notation: Python module and function separated by the dot.
3.141592653589793
>>> help(math.log) #Handy for figuring out how to use the module and function appropriately.
Help on built-in function log in module math:

log(...)
    log(x[, base])
    
    Return the logarithm of x to the given base.
    If the base not specified, returns the natural logarithm (base e) of x.

>>> log(12[,base])
SyntaxError: invalid syntax
>>> log10(12)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    log10(12)
NameError: name 'log10' is not defined
>>> math.log10(12)
1.0791812460476249
>>> math.log(2[,10])
SyntaxError: invalid syntax
>>> math.log(2[10])
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    math.log(2[10])
TypeError: 'int' object is not subscriptable
>>> 
>>> #Defining new functions
>>> #This function prints a string
>>> def print_string(): #Don't leave colon. It causes indentation on next line
	print ("Python Programming")
	print ("Super cool")

	
>>> #After defining print_string, we have to run or "call" the function:
>>> #After defining print_string(), we have to run or "call" the function.
>>> print_string()
Python Programming
Super cool
>>> 
>>> 
>>> #Execution Flow
>>> def WorkdayHours():
	print("Mon-Fri: 9-9")
def WeekendHours():
	
SyntaxError: invalid syntax
>>> def WorkdayHours():
	print("Mon-Fri: 9-9")
def WeekendHours():
	
SyntaxError: invalid syntax
>>> print
<built-in function print>
>>> """
#Execution Flow
def WorkdayHours():
  print ("Mon-Fri: 9-9")
def WeekendHours():
  print("Weekends: 11-5")

  #Call two previously defined functions
  def ShopHours():
    WorkdayHours()
    WeekendHours()

  #Call the function
  ShopHours()

  """
'\n#Execution Flow\ndef WorkdayHours():\n  print ("Mon-Fri: 9-9")\ndef WeekendHours():\n  print("Weekends: 11-5")\n\n  #Call two previously defined functions\n  def ShopHours():\n    WorkdayHours()\n    WeekendHours()\n\n  #Call the function\n  ShopHours()\n\n  '
>>> def WorkdayHours():
  print ("Mon-Fri: 9-9")
def WeekendHours():
  print("Weekends: 11-5")

  #Call two previously defined functions
  def ShopHours():
    WorkdayHours()
    WeekendHours()

  #Call the function
  ShopHours()
  
SyntaxError: invalid syntax
>>>  def WorkdayHours():
       print ("Mon-Fri: 9-9")
     def WeekendHours():
       print("Weekends: 11-5")

  #Call two previously defined functions
     def ShopHours():
       WorkdayHours()
       WeekendHours()

  #Call the function
  ShopHours()
  
SyntaxError: unexpected indent
>>> def WorkdayHours():
      print ("Mon-Fri: 9-9")
    def WeekendHours():
      print("Weekends: 11-5")

  #Call two previously defined functions
    def ShopHours():
      WorkdayHours()
      WeekendHours()

  #Call the function
  ShopHours()
  
SyntaxError: unindent does not match any outer indentation level
>>> def WorkdayHours():
	print ("Mon-Fri: 9-9")
def WeekendHours():
	
SyntaxError: invalid syntax
>>> 
>>> 
>>> def print_twice(bruce): #bruce here is a placeholder/ replaceable. 
	print(bruce)
	print(bruce)
	
	
	#A parameter is a variable. Arguments are the data you pass into the parameter. These can be the same or different. It's a placeholder for the actual argument.
	
[DEBUG ON]
>>> 
[DEBUG OFF]
>>> 
