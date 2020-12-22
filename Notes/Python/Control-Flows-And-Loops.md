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