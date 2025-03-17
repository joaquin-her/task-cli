import sys 

app_name = sys.argv[0]
first_argument = sys.argv[1]
second_argument = sys.argv[2]

def handle_add():
	print("add requested...")


match first_argument:
	case "add":
		handle_add()


print('Primer argumento:' + first_argument)
print('Segundo argumento:' + second_argument)
