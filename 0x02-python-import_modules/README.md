0. Import a simple function from a simple file
	- Write a program that imports the function `def add(a, b):` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3`
		- You have to use `print` function with string format to display integers
		- You have to assign:
			- the value `1` to a variable called `a`
			- the value `2` to a variable called `b`
		- `a` and `b` must be defined in 2 different lines: `a = 1` and another `b = 2`
		- Your program should print: `<a value> + <b value> = <add(a, b) value>` followed with a new line
		- YOU CAN ONLY SUE THE WORD `add_0` ONCE IN YOU CODE
		- You are not allowed to use `*` for importing or `__import__`
		- Your code should not be executed when imprted - by using `__import__`

1. My first toolbox!
	- Write a program that import functions from the file `calculator_1.py`, does some Maths, and prints the result.
		- Do not use the function `print` (with string format to display integers) more than 4 times
		- You have to define:
			- the value `10` to a variable `a`
			- the value `5` to a variable `b`
			- and use those two variables only, as arguments when calling functions (including `print`)
		- `a` and `b` must be defined in 2 different lines: `a = 10` and another `b = 5`
		- Your program should call each of the imported functions.
		- the word `calculator_1` should be used only once in your file
		- You are not allowed to use `*` for importing of `__import__`
		- Your code should not be executed when imported

2. How to make a script dynamic!
	- Write a program that prints the number of and the list of its arguments.
		- The ouput should be:
			- Number of argument(s) followed by `argument` (if number is one) or `arguments`(otherwise), followed by
			- `:` or `.` if no arguments were passed followed by
			- a new line, followde by (if at least on argument), 
			- one line per argument:
				- the position of the argument (starting a `1`) followed by `:`, followed by the argument value and a new line
		- Your code should not be executed when imported
		- The number of elements of `argv` can be retrieved by usin: `len(argv)`
