def mat_data(l):
	info= {"Density @STP": l[1]}
	return info

def massfract_data(line, l, lines):
	position = lines.index(line)
	number_of_ele =int(l[2])
	masses = []
	for i in range(number_of_ele):
		masses.append(lines[position+1+i].split())
	return masses

def library_creator(data_input): 
	
	file = open(data_input, "r+")

	lines = file.readlines()

	dandy = {}

	for line in lines:
		l = line.split()
		if line[0].isalpha():

			dandy[l[0]] = mat_data(l)
			dandy[l[0]].update({"Mass Fraction" : massfract_data(line, l, lines)})
	return(dandy)
