import turtle; #bring in the turtle library

window = turtle.Screen(); #create a variable for the window
my_turtle = turtle.Turtle(); #create a variable for your turtle

def Name(x, y):
	my_turtle.reset();
	for i in range(0,1):
		my_turtle.write("Xilun", True, "center",font=("Arial",24 ,"normal"));

my_turtle.onclick(Name);
window.mainloop(); #wait for the user to close the window
