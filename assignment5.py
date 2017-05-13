import turtle;

window = turtle. Screen();
window.bgcolor("purple");
window.title("turtles");

my_turtle = turtle.Turtle();
my_turtle.color("white");
my_turtle.pensize(5);
my_turtle.speed(8);

def star(x, y):
	my_turtle.reset();
	for i in range (0,5):
		my_turtle.forward(100);
		my_turtle.right(144);

my_turtle.onclick(star);

window.mainloop();
