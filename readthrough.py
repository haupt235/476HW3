import element_data as ed

file = open("elelib", "r+")

lines = file.readlines()

nice = {}

for line in lines:
	
	l = line.split()

	if line[0].isalpha():

		nice[l[0]] = ed.element_data(l)
#		nice[l[0]].update({"iso" : ed.isotope_data(line, l, lines)})

print(nice)


