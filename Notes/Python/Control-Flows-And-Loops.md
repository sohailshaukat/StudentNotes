# Control Flows

- Tools to manange flow of your execution
- Decisions based on conditions.
- Expression(Condition) -> Outcome(Result of Condition) 
- a+b = c -> equation
- Expression a+b =? , Question??? 
- **Comparison Operator**, it will lie between two objects or two set of objects and will yield a boolean result
- Conditional Expression -> Yes / No , 1/0, True/False
	- These are called booleans
		- Booleans in python are,**True** or **False**
		- Boolean itself is a data type in python
		- Any non zero value is **True**
		- Any non null item is **True**
	- Used to express binary situations
	- Existential comparison, comparing my object for it's existence
		- "zahid" == "sharik" -> False
		- "zahid" == "zahid" -> True
		- "Zahid" == "zahid" -> False
		- "Zahid".lower() == "zahid".lower() -> True
	- Degree based comparison
		- Greater (a>b), Lesser(a<b), Greater than or equals to (a>=b), Less than or equals to(a<=b).
		- Numeric situations mostly.
		- 5 > 7 -> False
		- 5 > 5 -> False
		- 5 >= 5 -> True
		- 5 < 7 -> True


# if
- If is used to regulate control flow.
```
if (conditional expression) :	 
	 # this part will be executed if conditional expression yields true.

```

# if-else
- If-else is used to regulate and provide an alternative flow when condition is not matched.
```
if (conditional expression) :	 
	# this part will be executed if conditional expression yields True
else:
	# this part will be executed if conditional expression yields False
```

# if-elif-else
- This can be used for multiple conditions, Athough multiple conditions can be implemented by nested if else, but this approach is simpler
```
if (conditional expression) :	 
	# this part will be executed if conditional expression yields True
elif (conditional expression 2):
	# this part will be executed if conditional expression 2 yields True
else:
	# this part will be executed if conditional expression yields False
```


## or
- Gives **True** if any in comparison are **True**
## and
- Gives **True** if all in comparison are **True**
## not 
- Inverses


# Loops
- To repeat a certain instruction(s).
- set of times
	- I want to click a button 5 times
- set of elements, I want to do something for each element in that collectible
	- I want to convert each letter in Zahid's name to uppercase
	- I want to find inverse of each integer in a list
	- I want to do something ```for each``` element


# For loop
- C, Java ``` for (i=0;i<9;i++){}```
	- ``` for (init, condi, inc/dec)```
	- ``` for (i=1; i<=10; i++) ```  this will yield 1-10
	- ``` for (i=1; i<=10; i++2) ```  this will yield 1,3,5,7,9
- Python
	- ```for element in iterable```
	- ```for i in range(11):``` this will yield 0-10
	- ```for i in range(1,11):``` this will yield 1-10
	- ```for i in range(1,11,2):``` this will yield 1,3,5,7,9
		- **range** : range returns a iterable.
			- Where 
				- First argument is lowerlimit
				- Second argument is upperlimit (exclude)
				- Third argument is step
	- ```for let in "zahid":``` let = z, a, h, i, d
	- ```for let in [1,2,3,4,5]:``` let = 1,2,3,4,5
	- ```for let in [(1,"a"),(2,"b"),(3,"c"),(4,"d"),(5,"e")]:``` let = (1,a) ,(2,b) ,(3,c) ,(4,d) , (5,e)
	- ```for l1, l2 in [(1,a),(2,b),(3,c),(4,d),(5,e)]:```
		- l1 = 1 ; l2 =a 
		- l1 = 2 ; l2 =b
	- Tuple unpacking :  name1, name2 = "zahid" , "sharik"
	- ![[Pasted image 20201224173504.png]]
	
# while loop
- C, Java ```while i<9```
	- ``` init; while condi{ inc/dec }```
	- Infinite loop ``` while condi=True ```
	```
	i = 1	#init
	while i < 11:	#condi
		print(i)
		i += 1	#inc/dec
	```
	- Working with iterable
	```
	s, i = "zahid", 0
	while i < len(s):
		print(s[i])
		i += 1
		
	results = [(1,"Fail"),(2,"Pass"),(3,"Fail"),(4,"Pass"),(5,"Fail")]		
	i = 0
	while i < len(results):
		print(results[i])
		i += 1	
		
	results = [(1,"Fail"),(2,"Pass"),(3,"Fail"),(4,"Pass"),(5,"Fail")]		
	i = 0
	while i < len(results):
		num, res = results[i]
		print(num, res)
		i += 1	
	```
	
	![[Pasted image 20201224174144.png]]
	![[Pasted image 20201224174058.png]]