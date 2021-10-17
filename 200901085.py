open_list = ["[","{","("]
close_list = ["]","}",")"]

# Function using stack class
def check(myStr):
	stack = []
	for i in myStr:
		if i in open_list:
			stack.append(i)
		elif i in close_list:
			pos = close_list.index(i)
			if ((len(stack) > 0) and
				(open_list[pos] == stack[len(stack)-1])):
				stack.pop()
			else:
				return "False"
	if len(stack) == 0:
		return "True"
	else:
		return "False"

string = "({a+b})"
print(string,"-", check(string))

string = "))((a+b}{"
print(string,"-", check(string))

string = "((a+b))"
print(string,"-",check(string))

string = "))"
print(string,"-",check(string))

string = "[a+b]*(x+2y){gg+kk}"
print(string,"-",check(string))
